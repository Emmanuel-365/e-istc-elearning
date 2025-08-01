from django import forms
from .models import Activite

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['title', 'description', 'activity_type', 'due_date']
