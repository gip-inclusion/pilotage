from django.contrib import admin
from django.utils.text import capfirst

from pilotage.surveys import models
from pilotage.surveys.utils import get_step_form_class
from pilotage.surveys.views import ESATStep


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "vintage", "created_at", "updated_at")
    list_filter = ("kind", "vintage")
    readonly_fields = ("name", "created_at", "updated_at")

    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "name",
                    "kind",
                    "vintage",
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


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("uid", "survey", "status", "created_at", "updated_at")
    list_filter = ("survey", "status")
    readonly_fields = ("uid", "created_at", "updated_at")

    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "uid",
                    "survey",
                    "status",
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


@admin.register(models.ESATAnswer)
class ESATAnswerAdmin(AnswerAdmin):
    def get_fieldsets(self, request, obj=None):
        steps_fieldsets = []
        for step in ESATStep:
            step_form_class = get_step_form_class(models.ESATAnswer, step)
            steps_fieldsets.append(
                (
                    f"Données - {capfirst(step.label)}",
                    {
                        "fields": step_form_class.Meta.fields,
                    },
                )
            )
        return super().get_fieldsets(request, obj) + tuple(steps_fieldsets)
