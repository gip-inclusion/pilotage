from django.shortcuts import get_object_or_404, render

from pilotage.surveys.models import Survey


def show(request, *, name):
    survey = get_object_or_404(Survey, name=name)
    return render(request, "surveys/survey.html", context={"survey": survey})
