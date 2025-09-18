from django import forms
from .models import Skill, Achievement, Certificate, StudentProfile

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'date', 'proof_link']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'issuer', 'issue_date', 'file', 'link']
        widgets = {'issue_date': forms.DateInput(attrs={'type': 'date'})}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['bio', 'college', 'avatar']
