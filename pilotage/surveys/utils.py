from pilotage.surveys import forms as survey_forms


KNOWN_ACRONYM = {
    "PMSMP",
    "OPCO",
    "CPF",
}


def get_step_form_class(answer_class, step):
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


def get_step_informations(steps, answer, exclude=None):
    informations = {}
    for step in steps:
        if exclude and step in exclude:
            continue
        form_class = get_step_form_class(answer.__class__, step)
        informations[step] = {
            "filled": len({f for f in form_class.Meta.fields if getattr(answer, f) not in [None, "", []]}),
            "total": len(form_class.Meta.fields),
        }
    return informations
