from django.contrib import admin
from django.utils.text import capfirst

from pilotage.surveys import models
from pilotage.surveys.utils import get_step_form_class
from pilotage.surveys.views import CommonStep, ESATStep


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "vintage", "is_open", "created_at", "updated_at")
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


def _get_esat_question_fields():
    """Compute the list of question fields and step names once."""
    question_fields = []
    step_names = []
    for step in ESATStep:
        if step in CommonStep:
            continue
        step_form_class = get_step_form_class(models.ESATAnswer, step)
        question_fields.extend(step_form_class.Meta.fields)
        step_names.append(step.value)
    return question_fields, step_names


_esat_question_fields, _esat_step_names = _get_esat_question_fields()


@admin.register(models.ESATAnswer)
class ESATAnswerAdmin(AnswerAdmin):
    list_display = ("uid", "survey", "answered_count", "created_at", "updated_at")

    @admin.display(description="Réponses")
    def answered_count(self, obj):
        answered = sum(
            1
            for field in _esat_question_fields
            if (value := getattr(obj, field, None)) is not None and value != "" and value != []
        )

        feedback_answered = 0
        if obj.step_feedback:
            feedback_answered = sum(1 for step in _esat_step_names if obj.step_feedback.get(step))

        total_fields = len(_esat_question_fields) + len(_esat_step_names)
        return f"{answered + feedback_answered}/{total_fields}"

    def get_fieldsets(self, request, obj=None):
        steps_fieldsets = []
        for step in ESATStep:
            if step in CommonStep:
                continue
            step_form_class = get_step_form_class(models.ESATAnswer, step)
            fields = list(step_form_class.Meta.fields) + [f"feedback_{step.value.replace('-', '_')}"]
            steps_fieldsets.append(
                (
                    f"Données - {capfirst(step.label)}",
                    {
                        "fields": fields,
                    },
                )
            )
        return super().get_fieldsets(request, obj) + tuple(steps_fieldsets)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        for step in ESATStep:
            if step in CommonStep:
                continue
            readonly_fields.append(f"feedback_{step.value.replace('-', '_')}")
        return readonly_fields

    def __getattr__(self, name):
        if name.startswith("feedback_"):
            step_name = name[9:].replace("_", "-")

            def feedback_field(obj):
                if obj and obj.step_feedback:
                    return obj.step_feedback.get(step_name, "-")
                return "-"

            feedback_field.short_description = "❓ Retours"
            return feedback_field
        raise AttributeError(name)
