import re

from django.core.exceptions import ValidationError

from pilotage.itoutils.algorithms import check_luhn


FINESS_RE = re.compile(
    r"""^
    [013-8]\d|2[AB]|9[0-58]0\d{6}  # Continental departments and Mayotte
    |970[1-5]\d{5}  # Other ultramarine departments
$""",
    re.VERBOSE,
)


def validate_siret(siret):
    if not siret.isdigit() or len(siret) != 14:
        raise ValidationError("Le numéro SIRET doit être composé de 14 chiffres.")


def validate_finess(finess):
    if len(finess) != 9:
        raise ValidationError("Le numéro FINESS doit être composé de 9 caractères.")
    if not FINESS_RE.match(finess):
        raise ValidationError("Le numéro FINESS n'a pas la structure attendue.")
    if not check_luhn(finess.replace("2A", "21").replace("2B", "22")):
        raise ValidationError("Le numéro FINESS contient une erreur.")
