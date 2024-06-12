from django.shortcuts import render
from . models import Student
from . serializers import StudetSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudetSerializer(stu, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

def student_list(request):
    stu = Student.objects.all()
    serializer = StudetSerializer(stu, many=True)
    print(serializer.data)
    
    # non dict dat, so safe = False
    return JsonResponse(serializer.data, safe=False)

# def student_detail(request, pk):
#     stu = Student.objects.get(id=pk)
#     serializer = StudetSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudetSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)