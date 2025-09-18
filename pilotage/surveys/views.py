from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pilotage.surveys.forms import ESATAnswerOrganizationForm
from pilotage.surveys.models import ESATAnswer, Survey, SurveyKind


def start(request, *, survey_name):
    survey = get_object_or_404(Survey, name=survey_name)
    if survey.kind == SurveyKind.ESAT:
        answer = ESATAnswer.objects.create(survey=survey)
    return redirect(reverse("surveys:tunnel", kwargs={"survey_name": survey.name, "answer_uid": answer.uid}))


def tunnel(request, *, survey_name, answer_uid):
    survey = get_object_or_404(Survey, name=survey_name)
    if survey.kind == SurveyKind.ESAT:
        answer = get_object_or_404(ESATAnswer, uid=answer_uid)
        form = ESATAnswerOrganizationForm(instance=answer, data=request.POST or None)
        title = "Votre organisation"

    return render(request, "surveys/survey.html", context={"survey": survey, "form": form, "title": title})
