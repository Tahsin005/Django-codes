from django.urls import path, include
# from .views import contact
from .import views
urlpatterns = [
    path('courses/', views.courses),
    path('about/', views.about),
    path('', views.home)
]
