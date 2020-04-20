from django.contrib import admin
from   .models import Attendance, Department , Employee 

# Register your models here.


admin.site.register (Attendance)
admin.site.register (Department)
admin.site.register (Employee) 