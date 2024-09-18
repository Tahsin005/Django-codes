from django.urls import path
from . import views
urlpatterns = [
    path('employeesList/', views.EmployeesList, name='EmployeesList')    ,
    path('employeeDetails/<int:id>', views.EmployeeDetails, name='EmployeeDetails'),
    path('employeeDelete/<int:id>', views.EmplyeeDelete, name='EmployeeDelete'),
    path('employeeInsert/', views.EmployeeInsert, name='EmployeeInsert'),
    path('employeeUpdate/<int:id>', views.EmployeeUpdate, name='EmployeeUpdate'),
    path('bulkEmployeeInsert/', views.BulkInsertDemo, name='BID'),
    
]
