from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    deptid=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)

    def __str__(self):
        return self.deptname
    
class EmployeeModel(models.Model):
    empid=models.IntegerField(primary_key=True)
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=30)
    gender= models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    dept= models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    emptype=models.CharField(max_length=20)
    address= models.CharField(max_length=20)

    def __str__(self):
        return self.firstname
