from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from . forms import ContactForm, FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    
    success_url = '/thankyou/'
    initial = {
        'name' : 'sonam',
        'email' : 'sonam@gmail.com',
        'msg' : 'Hello this is intital data filled in the form'
    }
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return HttpResponse('<h1>Message sent</h1>')
    
    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'