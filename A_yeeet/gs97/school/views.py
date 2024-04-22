from django.shortcuts import render
from . models import Student 

# Create your views here.
def home(request):
    
    print('Return : ', student_data)
    # print("SQL Query : ", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})