from django.urls import path
from .views import DashboardView, AttendanceCreate, AttendanceList, EmployeeCreate, EmployeeList, AttendancePdfView, EmployeePdfView, AttendanceTodayArchiveView


urlpatterns =[
         path('create/attendance', AttendanceCreate.as_view(),name ='create_attendance'),
         path('attendance/list', AttendanceList.as_view(),name ='attendance_list'),
         path('create/employee', EmployeeCreate.as_view(),name ='create_employee'),
         path('employee/list', EmployeeList.as_view(),name ='employee_list'),
         path('', DashboardView.as_view(),name ='dashboard'),        
         path('attendance/pdf', AttendancePdfView.as_view(),name ='attendance_pdf'),
         path('employee/pdf', EmployeePdfView.as_view(),name ='employee_pdf'),
         path('today/',
         AttendanceTodayArchiveView.as_view(),
         name="archive_today"),
      
] 