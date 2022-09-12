from cProfile import label
from dataclasses import fields
from django import forms

from crudapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={'roll':'Enter Roll','name':'Enter Name','age':'Enter Age','address':'Enter Address','city':'Enter City','state':'Enter State','zip':'Enter Zip'}