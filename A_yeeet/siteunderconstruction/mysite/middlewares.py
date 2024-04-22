from django.shortcuts import HttpResponse, render
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print('Call From Middleware Befor View')
        response = render(request, 'mysite/siteuc.html')
        print('Call From Middlware After View')
        return response