from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Student
from django.views.generic.base import TemplateView
from . forms import StudnetForm
# Create your views here.

class StudentCreateView(CreateView):
    form_class = StudnetForm
    template_name ='school/student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudnetForm
    template_name ='school/student_form.html'
    success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/create/'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'
    
class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanks_update.html'

    