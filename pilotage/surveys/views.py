from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pilotage.surveys import forms as survey_forms
from pilotage.surveys.models import Survey


def start(request, *, survey_name):
    survey = get_object_or_404(Survey, name=survey_name)
    match survey.kind:
        case _:
            return HttpResponseNotFound()
    return redirect(
        reverse(
            "surveys:tunnel",
            kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": list(step_class)[0]},
        )
    )


KNOWN_ACRONYM = set()


def _get_step_form_class(answer_class, step):
    step_as_camel_case = (
        step.replace("-", " ").title().replace(" ", "") if step.upper() not in KNOWN_ACRONYM else step.upper()
    )
    return getattr(survey_forms, f"{answer_class.__name__}{step_as_camel_case}Form")


def _get_previous_and_next_step(steps, current_step):
    choices = list(steps)
    try:
        next_step = choices[choices.index(current_step) + 1]
    except IndexError:
        next_step = None
    try:
        previous_step = choices[choices.index(current_step) - 1]
    except IndexError:
        previous_step = None
    return previous_step, next_step


def tunnel(request, *, survey_name, answer_uid, step):
    survey = get_object_or_404(Survey, name=survey_name)
    match survey.kind:
        case _:
            return HttpResponseNotFound()

    answer = get_object_or_404(answer_class, uid=answer_uid)
    try:
        step = steps_class(step)
    except ValueError:
        return HttpResponseRedirect(
            reverse(
                "surveys:tunnel",
                kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": list(steps_class)[0]},
            )
        )
    previous_step, next_step = _get_previous_and_next_step(steps_class, step)
    form = _get_step_form_class(answer_class, step)(instance=answer, data=request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse(
                "surveys:tunnel",
                kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": next_step},
            )
        )

    return render(
        request,
        "surveys/survey.html",
        context={
            "survey": survey,
            "answer": answer,
            "form": form,
            "title": step.label,
            "steps_class": steps_class,
            "previous_step_url": reverse(
                "surveys:tunnel", kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": previous_step}
            )
            if previous_step
            else None,
            "current_step": step,
            "next_step": next_step,
        },
    )
