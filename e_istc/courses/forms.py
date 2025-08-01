from django import forms
from .models import Course, Module, Ressource
from users.models import User

class CourseForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=User.objects.filter(role=User.Role.ENSEIGNANT),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['title', 'file', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }