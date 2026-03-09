from django import forms

from pilotage.itoutils.forms import EmptyPlaceholderFormMixin, LetteredLabelFormMixin
from pilotage.surveys import models
from pilotage.surveys.utils import get_field_text


class ESATBaseForm(LetteredLabelFormMixin, EmptyPlaceholderFormMixin, forms.ModelForm):
    def __init__(self, *args, editable, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True if not editable else field.disabled


class ESATAnswerOrganizationForm(ESATBaseForm):
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
            "nb_places_allowed",
            "nb_employee_worked",
            "nb_employee_shared",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nb_places_allowed"].widget.attrs["min"] = 0
        self.fields["nb_employee_worked"].widget.attrs["min"] = 0

        if kwargs["editable"]:
            self.fields["esat_role"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "esat_role", "placeholder"
            )
            self.fields["esat_name"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "esat_name", "placeholder"
            )
            self.fields["esat_siret"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "esat_siret", "placeholder"
            )
            self.fields["finess_num"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "finess_num", "placeholder"
            )
            self.fields["managing_organization_name"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "managing_organization_name", "placeholder"
            )
            self.fields["nb_employee_shared"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "nb_employee_shared", "placeholder"
            )


class ESATAnswerWorkersSupportedForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_acc",
            "nb_worker_half_time",
            "mean_worker_age",
            "mean_seniority",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mean_worker_age"].widget.attrs["min"] = 0
        self.fields["mean_worker_age"].widget.attrs["max"] = 80
        self.fields["mean_seniority"].widget.attrs["min"] = 0


class ESATAnswerWorkersNewForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_previous_mot",
            "nb_worker_new",
            "nb_worker_temporary",
        ]


class ESATAnswerEstablishmentDiscoveryForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_mispe_mdph",
            "nb_worker_mispe_rpe",
        ]


class ESATAnswerOrdinaryWorkingEnvironmentForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_willing_mot",
            "nb_worker_ft_job_seekers",
        ]


class ESATAnswerOrdinaryWorkingEnvironmentAndCustomersInvolvementForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "prescription_delegate",
            "pmsmp_refused",
            "nb_worker_pmsmp",
            "nb_worker_service",
            "nb_worker_mad_indiv",
            "nb_worker_with_public",
            "nb_worker_only_inside",
            "nb_worker_cumul_esat_ea",
            "nb_worker_cumul_esat_mot",
        ]


class ESATAnswerWorkersLeftForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_left",
            "nb_worker_left_ea",
            "nb_worker_left_private",
            "nb_worker_left_asso",
            "nb_worker_left_public",
            "nb_worker_left_other_reason",
            "nb_worker_cdi",
            "nb_worker_cdd",
            "nb_worker_interim",
            "nb_worker_prof",
            "nb_worker_apprentice",
            "nb_conv_exit_agreement",
            "nb_conv_exit_agreement_new",
            "nb_worker_esrp",
        ]


class ESATAnswerWorkersRightToReturnForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_reinteg",
            "nb_worker_reinteg_other",
            "nb_esat_agreement",
        ]


class ESATAnswerSupportHoursForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    support_themes = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "support_themes", "label"),
        choices=models.SupportThemes.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_support_hours",
            "support_themes",
        ]


class ESATAnswerFormationsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "contrib_opco",
            "pct_opco",
            "nb_worker_formation_opco",
            "opco_or_anfh_refusal",
            "nb_worker_cpf_unused",
            "cpf_unused_reason",
            "formation_cpf",
            "nb_worker_intern_formation",
            "formation_subject",
            "autodetermination_formation",
            "nb_worker_autodetermination",
            "autodetermination_external_formation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_opco"].widget.attrs["max"] = 100
        if kwargs["editable"]:
            self.fields["cpf_unused_reason"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "cpf_unused_reason", "placeholder"
            )
            self.fields["formation_cpf"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "formation_cpf", "placeholder"
            )
            self.fields["formation_subject"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "formation_subject", "placeholder"
            )


class ESATAnswerSkillsForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    skills_validation_type = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "skills_validation_type", "label"),  # noqa: E501
        choices=models.SkillsValidationType.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "skills_validation_type",
            "nb_worker_rae_rsfp",
            "nb_worker_vae",
            "after_skills_validation",
        ]


class ESATAnswerDuodaysForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_duoday",
            "nb_employee_reverse_duoday",
        ]


class ESATAnswerSkillsNotebookForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    software_financial_help = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "software_financial_help", "label"),  # noqa: E501
        choices=models.SoftwareFinancialHelp.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "skills_notebook",
            "software_financial_help",
            "software_financial_help_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs["editable"]:
            self.fields["software_financial_help_type"].widget.attrs["placeholder"] = get_field_text(
                "esat-2025", "software_financial_help_type", "placeholder"
            )


class ESATAnswerRetirementForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    retirement_preparation_actions = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "retirement_preparation_actions", "label"),  # noqa: E501
        choices=models.RetirementPreparationActions.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "retirement_preparation_actions",
            "retirement_preparation_nb_workers",
            "uaat_inscription",
            "pct_more_than50",
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if kwargs["editable"]:
                self.fields["retirement_preparation_actions"].widget.attrs["placeholder"] = get_field_text(
                    "esat-2025", "retirement_preparation_actions", "placeholder"
                )
            self.fields["pct_more_than50"].widget.attrs["max"] = 100


class ESATAnswerLanguageAccessibilityForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    documents_falclist = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "documents_falclist", "label"),  # noqa: E501
        choices=models.DocumentFALCList.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "documents_falclist",
        ]


class ESATAnswerWorkingConditionsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "worker_delegate",
            "worker_delegate_formation",
            "nb_delegate_hours",
            "worker_delegate_hours_credit",
            "mix_qvt_in_place",
        ]


class ESATAnswerProfitSharingForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "profit_sharing_bonus",
            "mean_pct_esat_rem",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mean_pct_esat_rem"].widget.attrs["max"] = 100


class ESATAnswerInsurancePolicyForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "foresight_in_place",
            "year_foresight_in_place",
        ]


class ESATAnswerMobilityProgramForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "annual_transport_budget",
            "nb_worker_transport",
            "nb_worker_mobility_inclusion_card",
            "nb_worker_driving_licence",
            "nb_worker_code",
        ]


class ESATAnswerVouchersForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "holiday_voucher",
            "holiday_voucher_annual_budget",
            "gift_voucher",
            "gift_voucher_annual_budget",
        ]


class ESATAnswerSundayWorkForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_worker_worked_sunday",
        ]


class ESATAnswerPartnershipAgreementsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "agreement_signed_ft",
            "agreement_signed_ea",
            "agreement_signed_dept_pae",
        ]


class ESATAnswerStaffForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    insertion_staff_funding = forms.MultipleChoiceField(
        required=False,
        label=get_field_text("esat-2025", "insertion_staff_funding", "label"),
        choices=models.BudgetFunding.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_insertion_staff",
            "nb_insertion_dispo",
            "insertion_staff_funding",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nb_insertion_staff"].widget.attrs["min"] = 0
        self.fields["nb_insertion_dispo"].widget.attrs["min"] = 0


class ESATAnswerCommercialOperationForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "annual_ca",
            "annual_ca_production",
            "annual_ca_service",
            "annual_ca_mad",
            "pct_ca_public",
            "budget_commercial",
            "budget_commercial_deficit",
            "budget_commercial_excedent",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_ca_public"].widget.attrs["max"] = 100


class ESATAnswerSocialActivityBudgetForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "budget_social",
            "budget_social_deficit",
            "budget_social_excedent",
        ]


class ESATAnswerInvestmentsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "budget_accessibility",
            "budget_diversity",
        ]


class ESATAnswerCommentsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "comments",
        ]
