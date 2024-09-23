from django.contrib import admin
from . models import Employee, PartTimeEmployee, OnSiteEmployees, State, City
# Register your models here.
admin.site.register(Employee)
admin.site.register(PartTimeEmployee)
admin.site.register(OnSiteEmployees)
admin.site.register(City)
admin.site.register(State)