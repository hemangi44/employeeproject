from django.contrib import admin
from .models import DepartmentModel
from .models import EmployeeModel

# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)