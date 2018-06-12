from django import forms

from apps.handbooks.admin import HandBookAdmin


class AbstractParameterForm(forms.ModelForm):
    param_type = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['param_type'].choices = self._meta.model.choices


class AbstractParameterAdmin(HandBookAdmin):
    form = AbstractParameterForm


class AbstractOperationAdmin(HandBookAdmin):
    pass