from django import forms
from .models import DepartmentModel
from .models import EmployeeModel

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields='__all__'

class EmployeeForm(forms.ModelForm):
    gender= forms.ChoiceField(choices=[('Male','Male'),('Female','Female')],widget=forms.RadioSelect())
    emptype=forms.ChoiceField(choices=[('Part Time','Part Time'),('Full Time','Full Tiime')],widget=forms.RadioSelect())

    class Meta:
        model= EmployeeModel
        fields='__all__'