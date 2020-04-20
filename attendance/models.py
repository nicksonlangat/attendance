from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)
level_choices = (
    ('intern', 'Intern'),
    ('junior', 'Junior'), 
    ('senior', 'Senior')
    
)

class Department(models.Model):
	person=models.ForeignKey(User, on_delete=models.CASCADE)
	number =models.PositiveIntegerField() 
	name= models.CharField(max_length=30)
	description =models.TextField()
	def __str__(self):
		return self.name
	class Meta:
		ordering =('number',) 

class Employee(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    head_of_department = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=100)
    phone=models.PositiveIntegerField()
    image=models.ImageField(upload_to='media/image_uploads/', default ='media/avatar.jpeg')
    level= models.CharField(max_length=8, choices=level_choices, blank=True)
    work_id=models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
         ordering =('work_id',) 

class Attendance(models.Model):
    head_of_department = models.ForeignKey(User , on_delete=models.SET_NULL, blank=True, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, )
    attendance = models.CharField(max_length=8, choices=attendance_choices, blank=True)
    created=models.DateField(auto_now_add=True) 
   
  
 




