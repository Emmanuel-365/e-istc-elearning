from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'matricule', 'specialite')

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.role == User.Role.ETUDIANT and not user.username:
            user.username = user.matricule or user.email # Fallback if matricule is also empty
        user.set_unusable_password()
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'matricule', 'specialite', 'is_active')