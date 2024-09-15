from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index, name="home"),
    path('index/', views.index, name="home"),
    path('showMessages/', views.ShowMoreMessages, name='showMessages'),
    path('useVariable/', views.UseVariablesAsMessage, name='useVariablesAsMessage'),
    path('getReqDemo/', views.GetReqDemo, name='getReqDemo'),
    path('showDateTimeInfo/', views.ShowDateTimeInfo, name='showDateTimeInfo'),
    path('loggingExample/', views.loggingExample, name='loggingExample'),
    path('ifTagDemo/', views.ifTagDemo, name='ifTagDemo'),
    path('forTagDemo/', views.showProducts, name='forTagDemo'),
    path('showUsers/', views.loadUsers, name='showUsers'),
    path('showUsers2/', views.loadUsers2, name='showUsers2'),
    path('showUserDetails/', views.loadUserDetails, name='showUserDetails'),
    path('passModel/', views.PassModelToTemplate, name='passModel'),
    path('bifDemo/', views.BuiltInFiltersDemo, name='bifDemo'),
    path('ctfDemo/', views.CustomFiltersDemo, name='ctfDemo'),
    path('testStaticFiles/', views.TestStaticFiles, name='testStaticFiles'),
]
