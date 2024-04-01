from django.contrib import admin
from django.urls import path, include
from course import views as cv 
from fees import views as fv 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include([
        path('learndj/', cv.learn_django),
        path('learnpy/', cv.learn_python),
    ])),
    path('fe/', include([
        path('feesdj/', fv.fees_django),
        path('feespy/', fv.fees_python),
    ])),
]
