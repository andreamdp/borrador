from django import forms
from models import *

class NuevoClienteForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Cliente

def delete_empty_value(f):
    if isinstance(f, models.ForeignKey):
        qs = f.formfield().queryset
        return forms.ModelChoiceField(queryset=qs, empty_label=None)
    else:
        return f.formfield()


