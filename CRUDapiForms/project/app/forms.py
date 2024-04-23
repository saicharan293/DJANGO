from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','age','gender']
        GENDER_CHOICES = [
            ('select','Select'),
            ('male', 'Male'),
            ('female', 'Female'),
            ('others', 'Others'),
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER_CHOICES,attrs={'class': 'form-control'}),
            }
