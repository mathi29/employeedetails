# operations/forms.py

from django import forms
from django.core.exceptions import ValidationError
from operations.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise ValidationError('Email must end with @example.com')
        return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 1:
            raise ValidationError('Name must have at least 1 character.')
        if len(name) > 30:
            raise ValidationError('Name cannot exceed 30 characters.')
        return name
