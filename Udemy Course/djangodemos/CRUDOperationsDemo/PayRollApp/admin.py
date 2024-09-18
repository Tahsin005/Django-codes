from django.contrib import admin
from . models import Employee, PartTimeEmployee
# Register your models here.
admin.site.register(Employee)
admin.site.register(PartTimeEmployee)