from django import forms
from django.core import validators
from sistema.models import Inscripcion

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'