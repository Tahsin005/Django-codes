from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('employee_create/', views.employee_create, name='employee_create'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/details/<int:employee_id>/', views.employee_details, name='employee_details'),
    path('/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)