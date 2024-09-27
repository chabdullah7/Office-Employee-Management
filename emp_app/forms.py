from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    fields=['id', 'first_name', 'last_name', 'department', 'role', 
            'email','phone_number', 'salary', 'joining_date']