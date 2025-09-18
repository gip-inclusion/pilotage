from django import forms

from pilotage.surveys import models


class ESATAnswerOrganizationForm(forms.ModelForm):
    esat_role = forms.CharField(
        label="Quelle est votre fonction au sein de l'ESAT?",
        widget=forms.TextInput(attrs={"placeholder": "Directrice d'ESAT"}),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "esat_role",
            "esat_name",
            "esat_siret",
            "finess_num",
            "managing_organization_name",
            "esat_status",
            "esat_dept",
        ]
