from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'


class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = 'sonam'
        context['roll'] = 101
        
        # extra context doesn't work in this format
        # context = {
        #     'name': 'Ferdous',
        #     'roll': 101,
        # }
        
        print(context)
        # print(kwargs)
        print(kwargs)
        return context