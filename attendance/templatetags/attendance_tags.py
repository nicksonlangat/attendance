from django import template
from django.shortcuts import render
from attendance.models import Employee
from django.contrib.auth.models import User
register=template.Library()
@register.simple_tag
def total_employees():
	count = Employee.objects.all().count()
	return count
	
@register.simple_tag
def total_users():
	user = User.objects.all().count()
	return user
	
@register.simple_tag
def my_employees():
	count = Employee.objects.filter(head_of_department=request.user).count()
	return count
	