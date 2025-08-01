from django import forms
from .models import Activite, Question, Choix

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['title', 'description', 'activity_type', 'due_date']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['intitule', 'type_question']

class ChoixForm(forms.ModelForm):
    class Meta:
        model = Choix
        fields = ['texte', 'est_correct']
