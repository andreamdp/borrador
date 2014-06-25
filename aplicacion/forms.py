from django import forms
from models import Residente, ResidenciaAut
from django.forms.models import inlineformset_factory
from django.views.generic.edit import FormView, CreateView


class ResidenteForm1(forms.ModelForm):
    tipoR = forms.IntegerField(initial=1, required=True)
    def __init__(self, *args, **kwargs):
        super(ResidenteForm1, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['residencia'].widget.attrs['disabled'] = 'disabled'
        self.fields['residencia'].widget = forms.HiddenInput()
        #self.fields['tipoR'].widget = forms.HiddenInput()
    class Meta:
        model =  Residente  
        fields = ('nombre', 'apellido','residencia')
        exclude=('tipoR',)
    def save(self):
        self.instance.tipoR = 1
        super(ResidenteForm1, self).save()
        
class ResidenteForm2(forms.ModelForm):
    tipoR = forms.IntegerField(initial=2, required=True)
    def __init__(self, *args, **kwargs):
        super(ResidenteForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['residencia'].widget.attrs['disabled'] = 'disabled'
        self.fields['residencia'].widget = forms.HiddenInput()
        #self.fields['tipoR'].widget = forms.HiddenInput()
    class Meta:
        model =  Residente  
        fields = ('nombre', 'apellido','residencia')
        exclude=('tipoR',)
    def save(self):
        self.instance.tipoR = 2
        super(ResidenteForm2, self).save()
        
class ResidenteForm3(forms.ModelForm):
    tipoR = forms.IntegerField(initial=3, required=True)
    def __init__(self, *args, **kwargs):
        super(ResidenteForm3, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['residencia'].widget.attrs['disabled'] = 'disabled'
        self.fields['residencia'].widget = forms.HiddenInput()
        #self.fields['tipoR'].widget = forms.HiddenInput()
    class Meta:
        model =  Residente  
        fields = ('nombre', 'apellido','residencia')
        exclude=('tipoR',)
    def save(self):
        self.instance.tipoR = 3
        super(ResidenteForm3, self).save()
        
class ResidenteForm4(forms.ModelForm):
    tipoR = forms.IntegerField(initial=4, required=True)
    def __init__(self, *args, **kwargs):
        super(ResidenteForm4, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['residencia'].widget.attrs['disabled'] = 'disabled'
        self.fields['residencia'].widget = forms.HiddenInput()
        #self.fields['tipoR'].widget = forms.HiddenInput()
    class Meta:
        model =  Residente  
        fields = ('nombre', 'apellido','residencia')
        exclude=('tipoR',)
    def save(self):
        self.instance.tipoR = 4
        super(ResidenteForm4, self).save()


