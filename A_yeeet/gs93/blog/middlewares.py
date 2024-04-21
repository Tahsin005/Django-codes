from django.shortcuts import render, HttpResponse

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('MOTHER____one time initialization_______')
        
    def __call__(self, request):
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is BROTHER before view')
        response = self.get_response(request)
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is BROTHER after view')
        print('*777777777777')
        return response
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('FATHER____one time initialization_______')
        
    def __call__(self, request):
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is FATHER before view')
        # response = self.get_response(request)
        response = HttpResponse('Khopri tor iska')
        print('This is FATHER after view')
        
        return response
    
class AmmuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('AMMU____one time initialization_______')
        
    def __call__(self, request):
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is AMMU before view')
        response = self.get_response(request)
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is AMMU after view')
        print('*777777777777')
        return response
    
    