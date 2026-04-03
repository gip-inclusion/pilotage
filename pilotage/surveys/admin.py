import csv

from django.contrib import admin
from django.db.models import Q
from django.http import HttpResponse
from django.urls import path, reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.http import content_disposition_header
from django.utils.text import capfirst

from pilotage.itoutils.departments import get_department_to_region
from pilotage.surveys import models
from pilotage.surveys.forms import ESATAnswerOrganizationForm
from pilotage.surveys.models import ESATAnswer
from pilotage.surveys.utils import get_step_form_class, get_steps_informations
from pilotage.surveys.views import CommonStep, ESATStep


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "vintage", "is_open", "title", "created_at", "updated_at")
    list_filter = ("kind", "vintage")
    readonly_fields = ("name", "is_open", "created_at", "updated_at")

    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "name",
                    "kind",
                    "vintage",
                    "opening_period",
                    "title",
                    "introduction",
                    "conclusion",
                )
            },
        ),
        ("Audit", {"fields": ("created_at", "updated_at")}),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj is not None:
            readonly_fields += ("kind", "vintage")
        return readonly_fields

    @admin.display(description="ouvert", boolean=True)
    def is_open(self, obj):
        return obj.is_open


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("uid", "survey", "created_at", "updated_at")
    list_filter = ("survey",)
    readonly_fields = ("uid", "created_at", "updated_at")

    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "uid",
                    "survey",
                )
            },
        ),
        ("Audit", {"fields": ("created_at", "updated_at")}),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj is not None:
            readonly_fields += ("survey",)
        return readonly_fields

    def has_change_permission(self, request, obj=None):
        return False


class FINESSFilledFilter(admin.SimpleListFilter):
    title = "FINESS remplis"
    parameter_name = "finess_filled"

    def lookups(self, request, model_admin):
        return (("yes", "Oui"), ("no", "Non"))

    def queryset(self, request, queryset):
        value = self.value()
        finess_not_filled = Q(finess_num=None) | Q(finess_num="")
        if value == "yes":
            return queryset.exclude(finess_not_filled)
        if value == "no":
            return queryset.filter(finess_not_filled)
        return queryset


@admin.register(models.ESATAnswer)
class ESATAnswerAdmin(AnswerAdmin):
    list_display = (
        "uid",
        "survey",
        "answered_count",
        "finess_num",
        "esat_siret",
        "esat_name",
        "managing_organization_finess",
        "created_at",
        "updated_at",
    )
    search_fields = ("uid", "finess_num", "esat_siret", "esat_name", "managing_organization_finess")
    list_filter = (FINESSFilledFilter, "esat_dept")
    change_list_template = "admin/surveys/change_list.html"

    def get_fieldsets(self, request, obj=None):
        steps_fieldsets = []
        for step in ESATStep:
            if step in CommonStep:
                continue
            step_form_class = get_step_form_class(models.ESATAnswer, step)
            steps_fieldsets.append(
                (
                    f"Données - {capfirst(step.label)}",
                    {
                        "fields": step_form_class.Meta.fields,
                    },
                )
            )
        links_fieldsets = tuple([("Liens utiles", {"fields": ("start_url",)})])
        return super().get_fieldsets(request, obj) + links_fieldsets + tuple(steps_fieldsets)

    @admin.display(description="Réponses")
    def answered_count(self, obj):
        steps_informations = get_steps_informations(ESATStep, obj, exclude=CommonStep)
        return f"{steps_informations.total_filled}/{steps_informations.total_fields}"

    @admin.display(description="URL d'entrée")
    def start_url(self, obj):
        url = reverse(
            "surveys:tunnel",
            kwargs={"survey_name": obj.survey.name, "answer_uid": obj.uid, "step": CommonStep.INTRODUCTION},
        )
        return format_html('<a href="{}">{}</a>', url, CommonStep.INTRODUCTION)

    def get_urls(self):
        return [
            path(
                "download/",
                self.admin_site.admin_view(self.download_answers),
                name="download_esat_answers",
            )
        ] + super().get_urls()

    def download_answers(self, request):
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": content_disposition_header(
                    as_attachment=True,
                    filename=f"esat_answers_{timezone.now():%Y-%m-%d_%H:%M}.csv",
                ),
            },
        )

        data = {}
        for obj in ESATAnswer.objects.exclude(Q(finess_num=None) | Q(finess_num="")):
            filled = get_steps_informations(ESATStep, obj, exclude=CommonStep).total_filled
            # Ignore answers with only FINESS and pre-filled data
            if filled == len(ESATAnswerOrganizationForm.LOCKED_FIELD_ON_FINESS_DATA) + 1:
                if all([getattr(obj, f) for f in ESATAnswerOrganizationForm.LOCKED_FIELD_ON_FINESS_DATA.values()]):
                    continue

            if filled > data.get(obj.finess_num, {}).get("Réponses", -1):
                data[obj.finess_num] = {
                    "FINESS": obj.finess_num,
                    "ID": obj.pk,
                    "Réponses": filled,
                    "Région": get_department_to_region().get(obj.esat_dept, ""),
                }

        rows = sorted(data.values(), key=lambda o: (o["Région"], o["FINESS"]))

        writer = csv.DictWriter(response, fieldnames=["Région", "FINESS", "ID", "Réponses"])
        writer.writeheader()
        writer.writerows(rows)
        return response
