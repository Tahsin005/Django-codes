from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SignUp, name="signup"),
]
