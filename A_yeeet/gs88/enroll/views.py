from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The one', 30)
#         mv = cache.get('movie')
#     return render(request, 'enroll/course.html', {'fm': mv})


# def home(request):
#     mv = cache.get_or_set('fees', 44, 30, version=2)
#     return render(request, 'enroll/course.html', {'fm': mv})


# def home(request):
#     data = {
#         'name': 'sonam',
#         'roll': 101,
#     }
#     cache.set_many(data, 30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'enroll/course.html', {'stu': sv})

# def home(request):
#     cache.delete('fees', version=2)
#     return render(request, 'enroll/course.html')



def home(request):
    cache.decr('roll', delta=1)
    rv = cache.get('roll')
    print(rv)
    return render(request, 'enroll/course.html')
