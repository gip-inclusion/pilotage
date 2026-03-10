import csv
import dataclasses
import functools
import pathlib
import typing

from django.utils.text import capfirst


KNOWN_ACRONYM = {
    "PMSMP",
    "OPCO",
    "CPF",
}


def get_step_form_class(answer_class, step):
    from pilotage.surveys import forms as survey_forms  # Import here because of circular import (`get_field_text()`)

    step_as_camel_case = (
        step.replace("-", " ").title().replace(" ", "") if step.upper() not in KNOWN_ACRONYM else step.upper()
    )
    return getattr(survey_forms, f"{answer_class.__name__}{step_as_camel_case}Form")


def get_previous_and_next_step(steps, current_step):
    choices = list(steps)
    current_step_index = choices.index(current_step)

    try:
        next_step = choices[current_step_index + 1]
    except IndexError:
        next_step = None
    previous_step = choices[current_step_index - 1] if current_step_index > 0 else None  # Don't cycle in reverse order

    return previous_step, next_step


@dataclasses.dataclass(frozen=True)
class StepInformations:
    filled: int
    total: int


@dataclasses.dataclass(frozen=True)
class StepsInformations:
    data: dict[typing.Any, StepInformations]
    total_fields: int
    total_filled: int

    def progress(self):
        return int((self.total_filled / self.total_fields) * 100)


def get_steps_informations(steps, answer, exclude=None):
    informations = {}
    for step in steps:
        if exclude and step in exclude:
            continue
        form_class = get_step_form_class(answer.__class__, step)
        informations[step] = StepInformations(
            filled=len({f for f in form_class.Meta.fields if getattr(answer, f) not in [None, "", []]}),
            total=len(form_class.Meta.fields),
        )
    return StepsInformations(
        data=informations,
        total_fields=sum(i.total for i in informations.values()),
        total_filled=sum(i.filled for i in informations.values()),
    )


@functools.cache
def get_survey_specs(survey_name):
    with pathlib.Path(__file__).parent.joinpath("specs", f"{survey_name}.csv").open() as f:
        reader = csv.DictReader(f, delimiter=",")
        return {r["field_name"]: r for r in reader}


def _lower_first_letter(text):
    return text[0].lower() + text[1:]


def get_field_text(survey_name, field_name, text_id):
    if text_id == "verbose_name":
        text_id = "label"
        transform = _lower_first_letter
    else:
        transform = capfirst

    try:
        return transform(get_survey_specs(survey_name)[field_name][f"field_{text_id}"])
    except KeyError:
        return None


def clean_finess_field_quoting(value):
    if not value:
        return None
    return value[2:-1]  # Remove starting `="` and ending `"`


def parse_finess_fields(line):
    return [clean_finess_field_quoting(field) for field in line.strip().split(";")]


@functools.cache
def get_finess_data():
    data = {}
    with pathlib.Path(__file__).parent.joinpath("data", "export_finess.csv").open(encoding="iso-8859-1") as f:
        next(f)  # Drop headers, there are in utf-8 while the rest of the file is in iso-8859-1...
        for line in f:
            fields = parse_finess_fields(line)
            data[fields[0]] = {
                "finess": fields[0],
                "siret": fields[1].replace(" ", "") if fields[1] else None,
                "name": fields[3],
                "postal_code": fields[7],
                "legal_form_code": fields[14],
                "legal_finess": fields[20],
            }
    return data
