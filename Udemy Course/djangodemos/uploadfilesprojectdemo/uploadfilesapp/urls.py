from django.urls import path
from . import views
urlpatterns = [
    path('employee_create/', views.employee_create, name='employee_create'),
]
