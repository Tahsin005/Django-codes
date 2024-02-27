from django.http import HttpResponse

def home (request):
    return HttpResponse("Hello, world. You're at the home page.")
def contact (request):
    # pass
    return HttpResponse("Hello, world. You're at the contact page.")