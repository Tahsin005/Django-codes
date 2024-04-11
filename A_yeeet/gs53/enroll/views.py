from django.shortcuts import render

# Create your views here.
def home(request, check):
    print(check)
    return render(request, 'enroll/home.html', {'check': check})
# def show_details(request, my_id):
#     print(my_id)
#     return render(request, 'enroll/show.html', {'id' : my_id})

def show_details(request, my_id):
    if my_id == 1:
        student = {'id' : my_id, 'name' : 'Tahsin'}
    if my_id == 2:
        student = {'id' : my_id, 'name' : 'Lilin'}
    if my_id == 3:
        student = {'id' : my_id, 'name' : 'Abrar'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id' : my_id, 'name' : 'Tahsin', 'info' : 'my_subid'}
    if my_id == 2 and my_subid == 6:
        student = {'id' : my_id, 'name' : 'Lilin', 'info' : 'my_subid'}
    if my_id == 3 and my_subid == 7:
        student = {'id' : my_id, 'name' : 'Abrar', 'info' : 'my_subid'}
    return render(request, 'enroll/show.html', student)
