"""
URL configuration for dbfirstapproachdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dbfirstapproachapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ShowCategories/', views.ShowCategories),
    path('ShowOrders/', views.RawSqlDemo),
    path('StoredProcedureDemo/', views.StoredProcedureDemo),
    path('filteringDemo/', views.FilteringQuerySetsDemo, name='FDM'),
    path('ordersWithAccordion/', views.TwoLevelAccordionDemo, name='OWA'),
    path('multiLevelAccordion/', views.MultiLevelAccordionDemo, name='OWA'),
    path('CachingDemo/', views.CachingDemo, name='OWA'),
    path('ShowOrdersUsingCTT/', views.ShowOrdersUsingCTT, name='CTT'),
    path('export_to_csv/', views.ExportToCSV, name='export_to_csv'),
    path('export_to_json/', views.ExportToJSON, name='export_to_json'),
    path('export_to_xls/', views.ExportToXLS, name='export_to_xls'),
    path('export_to_docx/', views.ExportToWord, name='export_to_docx'),
    # path('export_to_pdf/', views.ExportToPDF, name='export_to_pdf'),
]
