import datetime
from django.shortcuts import render
from django.http import HttpResponse

from djangobasicsapp.models import Authors
import requests

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Hello World From Django</h1>')

def ShowMoreMessages(request):
    return HttpResponse('<h1>This is the second page</h1><h2>This is the second page</h2><h3>This is the second page</h3>')

def UseVariablesAsMessage(self):
    Message = "<h1>Welcome to Django Development</h1>"
    Message += "<h2>This is the second page</h2>"
    Message += "<h3>This is the second page</h3>"
    Message += "<h4>This is the second page</h4>"
    Message += "<h5>This is the second page</h5>"
    Message += "<h6>This is the second page</h6>"
    
    return HttpResponse(Message)


def GetReqDemo(request):
    Message = ''
    if request.method == 'GET':
        if request.GET.get('Message'):
            Message = f'<h1>Message Received: {request.GET.get("Message")} </h1>'
        else:
            Message = 'No Message Received'
            
        if request.GET.get('Country'):
            Message += f'<h1> Country: {request.GET.get("Country")} </h1>'
        else:
            Message += ', No Country Received'
    return HttpResponse(Message)


def ShowDateTimeInfo(request):
    TodaysDate = datetime.now()
    
    templateFileName = "djangobasicsapp/ShowTimeInfo.html"
    
    dict = {
        'TodaysDate': TodaysDate,
    }
    
    return render(request, templateFileName, context=dict)


import logging
from datetime import date, datetime 

def loggingExample(request):
    logging.debug(f'Debug: I just entered into the view.. {datetime.now()}')
    logging.info(f'Info: Confirmation that things are working as expected.')
    logging.warning(f'Warning: An indication that something unexpected happened.')
    logging.error(f'Error: Due to more serious problem, the software have stopped working.')
    logging.critical(f'Critical: A serious error, indicating that the program itself may be unable to continue.')
    
    custom_logger = logging.getLogger('mycustom_logger')
    custom_logger.debug(f'Debug: I just entered into the view.. {datetime.now()}')
    custom_logger.info(f'Info: Confirmation that things are working as expected.')
    custom_logger.warning(f'Warning: An indication that something unexpected happened.')
    custom_logger.error(f'Error: Due to more serious problem, the software have stopped working.')
    custom_logger.critical(f'Critical: A serious error, indicating that the program itself may be unable to continue.')
    
    return HttpResponse("Logging Demo.")


def ifTagDemo(request):
    
    data = {
        'name': 'MD. Tahsin Ferdous',
        'isVisible': True,
        'loggedIn': True,
        'countryCode': 'BAN',
        'workExperience': 35,
    }
    
    templateFileName = 'djangobasicsapp/IfTagDemo.html'
    
    dict = {'Data': data}
    
    return render(request, templateFileName, context=dict)
    
def showProducts(request):
    products = []
    
    Processors = [
        {'Category': 'AMD', 'processors': [
            'Ryzen 3990',
            'Ryzen 3980',
            'Ryzen 3970',
            'Ryzen 3960',
        ]},
        {'Category': 'Intel', 'processors': [
            'Xeon 3990',
            'Xeon 3980',
            'Xeon 3970',
        ]}
    ]
    products.append({
        'productID': 1, 
        'productName': 'AMD Ryzen 3990',
        'quantity': 100,
        'unitsInStock': 50,
        'disContinued': False,
        'cost': 3000,
    })
    products.append({
        'productID': 2, 
        'productName': 'AMD Ryzen 3980',
        'quantity': 100,
        'unitsInStock': 50,
        'disContinued': False,
        'cost': 4000,
    })
    products.append({
        'productID': 3, 
        'productName': 'AMD Ryzen 3970',
        'quantity': 100,
        'unitsInStock': 50,
        'disContinued': False,
        'cost': 5000,
    })
    products.append({
        'productID': 4, 
        'productName': 'AMD Ryzen 3960',
        'quantity': 100,
        'unitsInStock': 50,
        'disContinued': False,
        'cost': 6000,
    })
    
    templateFileName = 'djangobasicsapp/showProducts.html'
    dict = {'Products': products, 'TotalProducts': len(products), 'Processors': Processors}
    return render(request, templateFileName, context=dict)


    
def loadUsers(request):
    templateFileName = 'djangobasicsapp/showUsers.html'
    respone = CallRestAPI()
    dict = {
        'users' : respone.json()
    }
    return render(request, templateFileName, context=dict)
    
def CallRestAPI():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users')
    return response



def index(request):
    return render(request, 'djangobasicsapp/index.html')

def loadUsers2(request):
    templateFileName = 'djangobasicsapp/showUsersAsCards.html'
    image = 'https://i.pravatar.cc/'
    response = CallRestAPI()
    dict = {
        'users' : response.json(),
        'image' : image,
    }
    return render(request, templateFileName, context=dict)

def CallRestAPI2(userid):
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users/{userid}')
    return response


def loadUserDetails(request):
    if request.method == 'POST':
        counter = int(request.POST.get('useridcounter'))
        
        if request.POST.get('btnNext'):
            counter += 1
            if counter > 10:
                counter = 1
        elif request.POST.get('btnPrevious'):
            counter -= 1
            if counter == 0:
                counter = 1
    else:
        counter = 1
    response = CallRestAPI2(counter)
    image = 'https://i.pravatar.cc/'
    templateFileName = 'djangobasicsapp/showUserDetails.html'
    dict = {
        'user' : response.json(),
        'image' : image,
    }
    return render(request, templateFileName, context=dict)
    
    
    
    
def PassModelToTemplate(request):
    obj = Authors()
    obj.custom_init("Tahsin", "Bangladesh", "Coxs Bazar")
    templateFileName = 'djangobasicsapp/passModel.html'
    Dict = {"Author": obj}
    return render(request, templateFileName, Dict)
    
def BuiltInFiltersDemo(request):
    Processors = [
        {
            'name': 'Ryzen 3930',
            'cores': 32
        },
        {
            'name': 'Ryzen 3950',
            'cores': 16
        },
        {
            'name': 'Ryzen 3980',
            'cores': 64
        },
    ]
    
    dict = {
        'ProbationPeriod': 4,
        'FirstName': 'MD. Tahsin',
        'LastName': 'Ferdous',
        'PayForFight': 123456,
        'FirstQuarter': ['Jan', 'Feb', 'Mar'],
        'SecondQuarter': ['Apr', 'May', 'Jun'],
        'FQuarter': [1, 2, 3],
        'SQuarter': [4, 5, 6],
        'AboutMe': "i'm Notorious and I'm Ruthless too!",
        'now': datetime.now(),
        'PreviousFight': "",
        'NextFight': None,
        'Processors': Processors,
        'Message': '<h1>I am using escape</h1>',
        'website': 'https://www.uiacademy.co.in/'
    }
    return render(request, 'djangobasicsapp/BIFDemo.html', dict)


def CustomFiltersDemo(request):
    webframeworks = {
        'Description': 'Django is a Python framework  that makes it easier to create dynamic websites',
        'InDemand': '4.8',
        'PollNumber': 57650
    }
    return render(request, 'djangobasicsapp/testCustomFilters.html', webframeworks )


def TestStaticFiles(request):
    return render(request, 'djangobasicsapp/testStaticFiles.html')