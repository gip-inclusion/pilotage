import string


class EmptyPlaceholderFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["placeholder"] = ""


class LetteredLabelFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for idx, field in enumerate(self.fields.values()):
            field.label = f"{string.ascii_lowercase[idx]}. {field.label}"
