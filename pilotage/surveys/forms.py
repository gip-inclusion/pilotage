from django import forms

from pilotage.itoutils.forms import EmptyPlaceholderFormMixin, LetteredLabelFormMixin
from pilotage.surveys import models


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
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nb_places_allowed"].widget.attrs["min"] = 0
        self.fields["nb_employee_worked"].widget.attrs["min"] = 0

        if kwargs["editable"]:
            self.fields["esat_role"].widget.attrs["placeholder"] = "Directrice d'ESAT"
            self.fields["esat_name"].widget.attrs["placeholder"] = "ESAT Les pruniers"
            self.fields["esat_siret"].widget.attrs["placeholder"] = "12002701600357"
            self.fields["finess_num"].widget.attrs["placeholder"] = "123456789"
            self.fields["managing_organization_name"].widget.attrs["placeholder"] = "ADAPEI16"


class ESATAnswerWorkersSupportedForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_acc",
            "mean_employee_age",
            "mean_seniority",
            "nb_employee_half_time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mean_employee_age"].widget.attrs["min"] = 0
        self.fields["mean_employee_age"].widget.attrs["max"] = 80
        self.fields["mean_seniority"].widget.attrs["min"] = 0


class ESATAnswerWorkersNewForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_ordinary_job",
            "nb_employee_new",
            "nb_employee_temporary",
        ]


class ESATAnswerEstablishmentDiscoveryForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_mispe_mdph",
            "nb_employee_mispe_rpe",
        ]


class ESATAnswerOrdinaryWorkingEnvironmentForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_willing_ordinary",
            "nb_employee_ft_job_seekers",
        ]


class ESATAnswerOrdinaryWorkingEnvironmentAndCustomersInvolvementForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "prescription_delegate",
            "pmsmp_refused",
            "nb_employee_pmsmp",
            "nb_employee_service",
            "nb_employee_dispo_indiv",
            "nb_employee_dispo_collec",
            "nb_employee_restau",
            "nb_worker_only_inside",
            "pct_activity_outside",
            "nb_employee_cumul_esat_ea",
            "nb_employee_cumul_esat_ordi",
        ]


class ESATAnswerWorkersLeftForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_left",
            "nb_employee_left_ea",
            "nb_employee_left_private",
            "nb_employee_left_public",
            "nb_employee_left_asso",
            "nb_worker_left_other_reason",
            "nb_employee_cdi",
            "nb_employee_cdd",
            "nb_employee_interim",
            "nb_employee_prof",
            "nb_employee_apprentice",
            "nb_conv_exit",
            "nb_conv_exit_agreement_new",
            "nb_employee_left_esrp",
        ]


class ESATAnswerWorkersRightToReturnForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_reinteg",
            "nb_employee_reinteg_other",
            "nb_worker_other_esat_with_agreement",
            "nb_esat_conv",
        ]


class ESATAnswerSupportHoursForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_support_hours",
            "support_themes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nb_support_hours"].widget.attrs["min"] = 0
        if kwargs["editable"]:
            self.fields["support_themes"].widget.attrs["placeholder"] = (
                "Connaissance de soi et valorisation des compétences, accès aux droits, journée sportive"
            )


class ESATAnswerFormationsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "contrib_opco",
            "pct_opco",
            "nb_employee_formation_opco",
            "opco_or_anfh_refusal",
            "nb_employeed_cpf_unused",
            "cpfreason",
            "formation_cpf",
            "nb_employee_intern_formation",
            "formation_subject",
            "autodetermination_formation",
            "nb_employee_autodetermination",
            "autodetermination_external_formation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_opco"].widget.attrs["max"] = 100
        if kwargs["editable"]:
            self.fields["cpfreason"].widget.attrs["placeholder"] = "Nous n'avons eu aucune demande en ce sens"
            self.fields["formation_cpf"].widget.attrs["placeholder"] = "Permis de conduire"
            self.fields["formation_subject"].widget.attrs["placeholder"] = (
                "Hygiène, communication bienveillante, savoir s'exprimer en public"
            )


class ESATAnswerSkillsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "skills_validation_type",
            "nb_employee_rae",
            "nb_employee_rsfp",
            "after_reco_situation_list",
        ]


class ESATAnswerDuodaysForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_duoday",
            "nb_employee_reverse_duoday",
        ]


class ESATAnswerSkillsNotebookForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "duoday_board",
            "duoday_software_used",
            "software_name",
            "duoday_software_financial_help",
            "duoday_financial_help_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs["editable"]:
            self.fields["duoday_software_used"].widget.attrs["placeholder"] = "WIKIKAP, Neopass"
            self.fields["duoday_financial_help_type"].widget.attrs["placeholder"] = "CNR"


class ESATAnswerRetirementForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "retirement_preparation",
            "uaat_inscription",
            "nb_uaat_beneficiary",
            "pct_more_than50",
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if kwargs["editable"]:
                self.fields["retirement_preparation"].widget.attrs["placeholder"] = (
                    "Avenir après le travail, RDV CARSAT"
                )
            self.fields["pct_more_than50"].widget.attrs["max"] = 100


class ESATAnswerLanguageAccessibilityForm(ESATBaseForm):
    # TODO: Check if we can only override the widget
    documents_falclist = forms.MultipleChoiceField(
        required=False,
        label=(
            "au 31 décembre N-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils "
            "accessibles en FALC ou en communication alternative augmentée ? "
            "(contrat d’accompagnement par le travail, livret d’accueil, règlement de fonctionnement, etc.)"
        ),
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
            "employee_delegate",
            "employee_delegate_formation",
            "employee_delegate_hours_credit",
            "nb_delegate_hours",
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
            "nb_employee_transport",
            "nb_employee_mobility_inclusion",
            "nb_employee_driving_licence",
            "nb_employee_code",
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
            "nb_employee_worked_sunday",
        ]


class ESATAnswerPartnershipAgreementsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "rpe_convention_signed",
            "pea_convention_signed",
            "esat_pea_rattached",
            "ea_convention_signed",
            "nb_ea_convention_signed",
        ]


class ESATAnswerStaffForm(ESATBaseForm):
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
            "annual_ca_dispo",
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
            "budget_accessibility",
            "budget_diversity",
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
