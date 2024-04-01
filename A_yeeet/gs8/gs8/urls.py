from django.contrib import admin
from django.urls import path, include
from course import views as cv 
from fees import views as fv 

coursepatterns = [
        path('learndj/', cv.learn_django),
        path('learnpy/', cv.learn_python),
    ]
feespatterns = [
        path('feesdj/', fv.fees_django),
        path('feespy/', fv.fees_python),
    ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include(coursepatterns)),
    path('fe/', include(feespatterns)),
]
