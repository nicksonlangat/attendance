from django.contrib.auth.models import User
from .models import Attendance, Employee 
from django.forms import ModelForm 
from django import forms 



class AttendanceCreateForm(forms.ModelForm):
    class Meta:
       model = Attendance
       fields = ['employee', 'attendance']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(AttendanceCreateForm, self).__init__(*args, **kwargs)
       self.fields['employee'].queryset = Employee.objects.filter(head_of_department =user)