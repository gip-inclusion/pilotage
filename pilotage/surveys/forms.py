from django import forms

from pilotage.itoutils.forms import EmptyPlaceholderFormMixin, LetteredLabelFormMixin
from pilotage.surveys import models


class ESATBaseForm(LetteredLabelFormMixin, EmptyPlaceholderFormMixin, forms.ModelForm):
    pass


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
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["esat_role"].widget.attrs["placeholder"] = "Directrice d'ESAT"
        self.fields["esat_name"].widget.attrs["placeholder"] = "ESAT Les pruniers"
        self.fields["esat_siret"].widget.attrs["placeholder"] = "12002701600357"
        self.fields["finess_num"].widget.attrs["placeholder"] = "123456789"
        self.fields["managing_organization_name"].widget.attrs["placeholder"] = "ADAPEI16"


class ESATAnswerEmployeeForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_places_allowed",
            "nb_employee_worked",
            "nb_employee_acc",
            "mean_employee_age",
            "mean_seniority",
            "nb_employee_ordinary_job",
            "nb_employee_new",
            "nb_employee_temporary",
            "nb_employee_willing_ordinary",
            "nb_employee_ft_job_seekers",
            "nb_employee_mispe_mdph",
            "nb_employee_mispe_rpe",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nb_places_allowed"].widget.attrs["min"] = 0
        self.fields["nb_employee_worked"].widget.attrs["min"] = 0
        self.fields["mean_employee_age"].widget.attrs["min"] = 0
        self.fields["mean_employee_age"].widget.attrs["max"] = 80
        self.fields["mean_seniority"].widget.attrs["min"] = 0


class ESATAnswerPMSMPForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "prescription_delegate",
            "pmsmp_refused",
            "nb_employee_pmsmp",
        ]


class ESATAnswerActivityKindForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_service",
            "nb_employee_dispo_indiv",
            "nb_employee_dispo_collec",
            "nb_employee_restau",
        ]


class ESATAnswerPartialWorkForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "pct_activity_outside",
            "nb_employee_half_time",
            "nb_employee_cumul_esat_ea",
            "nb_employee_cumul_esat_ordi",
        ]


class ESATAnswerEmployeeLeftForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_left",
            "nb_employee_left_ea",
            "nb_employee_left_private",
            "nb_employee_left_public",
            "nb_employee_left_asso",
        ]


class ESATAnswerEmployeeReturnForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_reinteg",
            "nb_employee_reinteg_other",
            "nb_esat_conv",
        ]


class ESATAnswerMiscForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_conv_exit",
            "nb_employee_left_esrp",
            "nb_support_hours",
            "support_themes",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["support_themes"].widget.attrs["placeholder"] = (
            "Connaissance de soi et valorisation des compétences, accès aux droits, journée sportive"
        )


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
            self.fields["retirement_preparation"].widget.attrs["placeholder"] = "Avenir après le travail, RDV CARSAT"
            self.fields["pct_more_than50"].widget.attrs["max"] = 100


class ESATAnswerOPCOForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "contrib_opco",
            "pct_opco",
            "nb_employee_formation_opco",
            "opco_or_anfh_refusal",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_opco"].widget.attrs["max"] = 100


class ESATAnswerSkillsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_rae",
            "nb_employee_rsfp",
            "after_reco_situation_list",
        ]


class ESATAnswerCPFForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employeed_cpf_unused",
            "cpfreason",
            "formation_cpf",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cpfreason"].widget.attrs["placeholder"] = "Nous n'avons eu aucune demande en ce sens"
        self.fields["formation_cpf"].widget.attrs["placeholder"] = "Permis de conduire"


class ESATAnswerAutodeterminationForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_intern_formation",
            "formation_subject",
            "autodetermination_formation",
            "nb_employee_autodetermination",
            "autodetermination_external_formation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["formation_subject"].widget.attrs["placeholder"] = (
            "Hygiène, communication bienveillante, savoir s'exprimer en public"
        )


class ESATAnswerDuodayForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_employee_duoday",
            "duoday_board",
            "duoday_software_used",
            "duoday_software_financial_help",
            "duoday_financial_help_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["duoday_software_used"].widget.attrs["placeholder"] = "WIKIKAP, Neopass"
        self.fields["duoday_financial_help_type"].widget.attrs["placeholder"] = "CNR"


class ESATAnswerRepresentativeForm(ESATBaseForm):
    documents_falclist = forms.MultipleChoiceField(
        required=False,
        label=(
            "Au 31 décembre 2024, les principaux documents destinés aux travailleurs et travailleuses "
            "étaient-ils accessibles en FALC ou en communication alternative augmentée ?"
        ),
        choices=models.DocumentFALCList.choices,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = models.ESATAnswer
        fields = [
            "documents_falclist",
            "employee_delegate",
            "employee_delegate_formation",
            "employee_delegate_hours_credit",
            "nb_delegate_hours",
            "mix_qvt_in_place",
        ]


class ESATAnswerBonusForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "profit_sharing_bonus",
            "mean_pct_esat_rem",
            "pct_employee_activity_bonus",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mean_pct_esat_rem"].widget.attrs["max"] = 100
        self.fields["pct_employee_activity_bonus"].widget.attrs["max"] = 100


class ESATAnswerHealthAssuranceForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "health_complementary",
            "pct_health_complementary_esat",
            "annual_health_complementary_budget",
            "foresight_in_place",
            "year_foresight_in_place",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_health_complementary_esat"].widget.attrs["max"] = 100


class ESATAnswerMobilityForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "annual_transport_budget",
            "nb_employee_transport",
            "nb_employee_mobility_inclusion",
            "nb_employee_driving_licence",
            "nb_employee_code",
        ]


class ESATAnswerVoucherForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "holiday_voucher",
            "holiday_voucher_annual_budget",
            "gift_voucher",
            "gift_voucher_annual_budget",
        ]


class ESATAnswerConventionForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "rpe_convention_signed",
            "pea_convention_signed",
            "esat_pea_rattached",
            "ea_convention_signed",
            "nb_ea_convention_signed",
        ]


class ESATAnswerCounselorsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "nb_insertion_staff",
            "nb_insertion_dispo",
        ]


class ESATAnswerRevenueForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "annual_ca",
            "annual_ca_production",
            "annual_ca_service",
            "annual_ca_dispo",
            "pct_ca_public",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pct_ca_public"].widget.attrs["max"] = 100


class ESATAnswerSalesBudgetForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "budget_commercial",
            "budget_commercial_deficit",
            "budget_commercial_excedent",
        ]


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


class ESATAnswerCommentsForm(ESATBaseForm):
    class Meta:
        model = models.ESATAnswer
        fields = [
            "comments",
        ]
