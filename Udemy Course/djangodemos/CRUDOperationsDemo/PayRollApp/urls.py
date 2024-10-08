from django.urls import path
from . import views
urlpatterns = [
    path('employeesList/', views.EmployeesList, name='EmployeesList')    ,
    path('employeeDetails/<int:id>', views.EmployeeDetails, name='EmployeeDetails'),
    path('employeeDelete/<int:id>', views.EmplyeeDelete, name='EmployeeDelete'),
    path('employeeInsert/', views.EmployeeInsert, name='EmployeeInsert'),
    path('employeeUpdate/<int:id>', views.EmployeeUpdate, name='EmployeeUpdate'),
    path('bulkEmployeeInsert/', views.BulkInsertDemo, name='BID'),
    path('newBulkEmployeeInsert/', views.NewBulkInsertDemo, name='NBID'),
    path('bulkEmployeeUpdate/', views.BulkUpdationDemo, name='BUD'),
    path('bulkDeleteDemo/', views.BulkDeleteDemo, name='BDD'),
    path('deleteUsingRadio/', views.DeleteUsingRadio, name='DUR'),
    path('pageWiseEmpList/', views.PageWiseEmployeeList, name='PWEL'),
    path('cascadingselect/', views.cascadingSelect, name='cs'),
    path('load_states/', views.load_states, name='load_states'),
    path('load_cities/', views.load_cities, name='load_cities'),
    path('transactionDemo/', views.TransactionDemo, name='TD'),
    
]
 