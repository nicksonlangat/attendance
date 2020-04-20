from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView 
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User 
from  .models import Attendance,Department, Employee 
from django_xhtml2pdf.views import PdfMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



class DashboardView(TemplateView):
	template_name ='dashboard.html'
	
class EmployeeCreate(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    model = Employee
    fields ='__all__' 
    template_name ='employee/create_employee.html'
    success_message = "Employee Added!" 
    success_url = '/employee/list'
       
    def form_valid(self, form):   #the current logged in user will automatically be added as the doc author 
        form.instance.head_of_department = self.request.user
        return super().form_valid(form)

   
class EmployeeList(LoginRequiredMixin,ListView):
	model =Employee
	template_name ='employee/employee_list.html'
	
	
	def get_queryset(self):
		queryset =Employee.objects.all()
		user =self.request.user
		
		if not user.is_superuser:
			queryset = queryset.filter(
			    head_of_department=self.request.user 
			)
		return queryset  

class EmployeePdfView(LoginRequiredMixin, PdfMixin,ListView):
    model = Employee
    template_name = "employee/employee_pdf.html"
    
    def get_queryset(self):
        queryset =Employee.objects.all()
        user =self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(head_of_department=self.request.user)
        return queryset
		
class AttendanceList(LoginRequiredMixin,ListView):
	model =Attendance 
	template_name ='attendance/attendance_list.html'
	
	
	def get_queryset(self): #hod will only see his employees not anyone else's 
		queryset =Attendance.objects.all()
		user =self.request.user
		
		if not user.is_superuser:
			queryset = queryset.filter(
			    head_of_department=self.request.user 
			)
		return queryset 
            
class AttendanceCreate(LoginRequiredMixin, SuccessMessageMixin ,CreateView):
    model = Attendance
   # form_class =AttendanceCreateForm 
    fields =['employee', 'attendance'] 
    template_name ='attendance/attendance_create.html'  
    success_url ='/attendance/list'
    success_message = "Attendance marked!" 
    
    def get_form(self, *args, **kwargs):  #filter only employees added by the hod 
        form = super(AttendanceCreate, self).get_form(*args, **kwargs)
        form.fields['employee'].queryset = Employee.objects.filter(head_of_department =self.request.user)
        return form
        
    def form_valid(self, form):   #the current logged in user will automatically be added as the doc author 
        form.instance.head_of_department = self.request.user
        return super().form_valid(form)
           
        
from django.views.generic.dates import TodayArchiveView

class AttendanceTodayArchiveView(LoginRequiredMixin, TodayArchiveView):
    model = Attendance
    date_field = "created"
    allow_future = True
    def get_queryset(self):
        queryset =Attendance.objects.all()
        user =self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(head_of_department=self.request.user)
        return queryset
    
class AttendancePdfView(LoginRequiredMixin, PdfMixin,TodayArchiveView):
    model = Attendance
    template_name = "attendance/attendance_pdf.html"
    date_field = "created"
    def get_queryset(self):
        queryset =Attendance.objects.all()
        user =self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(head_of_department=self.request.user)
        return queryset