from django import forms
from .models import Version


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        labels = {
            'version_number': 'Versión',
            'date': 'Fecha',
            'summary': 'Resumen',
        }
