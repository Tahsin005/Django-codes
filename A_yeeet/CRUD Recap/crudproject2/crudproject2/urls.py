from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UseAddShowView.as_view(), name="addandshow"),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    path('<int:id>/', views.UserUpdateDataView.as_view(), name="updatedata"),
]
