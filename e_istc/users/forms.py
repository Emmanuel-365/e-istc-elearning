from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'matricule', 'specialite', 'photo')

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
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'matricule', 'specialite', 'is_active', 'photo')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'matricule', 'specialite', 'photo')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable matricule and specialite fields based on user role
        if self.instance.role == User.Role.ETUDIANT:
            self.fields['specialite'].required = False
            self.fields['specialite'].widget = forms.HiddenInput()
        elif self.instance.role == User.Role.ENSEIGNANT:
            self.fields['matricule'].required = False
            self.fields['matricule'].widget = forms.HiddenInput()
        else: # Admin or other roles, hide both
            self.fields['matricule'].required = False
            self.fields['matricule'].widget = forms.HiddenInput()
            self.fields['specialite'].required = False
            self.fields['specialite'].widget = forms.HiddenInput()
