from django.shortcuts import render
from . models import Categories, Orders, OrderDetails, Employees
import pyodbc

from django.db.models import Q, Avg, Sum, Min, Max, Count
# Create your views here.
def ShowCategories(request):
    categories = Categories.objects.all()
    
    return render(request, 'dbfa/ShowCategories.html', {'categories': categories}) 

def RawSqlDemo(request):
    query = '''
    SELECT a.OrderID, a.OrderDate, b.CompanyName, c.ProductName, d.UnitPrice, d.Quantity, d.UnitPrice * d.Quantity as 'BillAmount'
    FROM orders a inner join [order details] d on a.orderid = d.orderid inner join customers b on a.customerid=b.customerid inner
    join products c on d.productid=c.productid WHERE a.orderid between 10248 and 10255
    '''
    cnxn = GetConnection()
    cursor = cnxn.cursor()
    cursor.execute(query)
    orders = cursor.fetchall()
    
    cursor.close()
    cnxn.close()
    return render(request, 'dbfa/ShowOrders.html', {'Orders': orders})

def StoredProcedureDemo(request):
    
    GrandTotal = 0
    runningTotal = 0
    runningOrderTotal = 0
    
    cnxn = GetConnection()
    cursor = cnxn.cursor()
    cursor.execute("{call USP_GetAllOrders}")
    orders = cursor.fetchall()
    
    newOrders = [] 
    previousOrderID = 0
    subtotal = 0
    
    for order in orders:
        if previousOrderID == 0:
            previousOrderID = order.OrderID
            runningTotal += order.BillAmount
            runningOrderTotal += order.BillAmount
            GrandTotal += order.BillAmount
            subtotal += order.BillAmount
            newOrders.append(pushData(order, runningTotal, runningOrderTotal))
        elif previousOrderID == order.OrderID:
            runningTotal += order.BillAmount
            runningOrderTotal += order.BillAmount
            GrandTotal += order.BillAmount
            subtotal += order.BillAmount
            newOrders.append(pushData(order, runningTotal, runningOrderTotal))
        else:
            newOrders.append(pushData(0, runningTotal, 0))
            subtotal = 0
            previousOrderID = order.OrderID
            runningOrderTotal = 0
            
            runningTotal += order.BillAmount
            runningOrderTotal += order.BillAmount
            GrandTotal += order.BillAmount
            subtotal += order.BillAmount
            newOrders.append(pushData(order, runningTotal, runningOrderTotal))
            
    newOrders.append(pushData(0, runningTotal, 0))
    cursor.close()
    cnxn.close()
        
    return render(request, 'dbfa/ShowOrders.html', {'Orders': newOrders, 'GrandTotal': GrandTotal})

def pushData(order, runningTotal, runningOrderTotal):
    if order == 0:
        return {
            'OrderID': '',
            'OrderDate': '',
            'CompanyName': '',
            'ProductName': '',
            'UnitPrice': '',
            'Quantity': '',
            'BillAmount': '',
            'RunningTotal': runningTotal,
            'RunningOrderTotal': ''
        }
    else:
        return {
            'OrderID': order.OrderID,
            'OrderDate': order.OrderDate,
            'CompanyName': order.CompanyName,
            'ProductName': order.ProductName,
            'UnitPrice': order.UnitPrice,
            'Quantity': order.Quantity,
            'BillAmount': order.BillAmount,
            'RunningTotal': runningTotal,
            'RunningOrderTotal': runningOrderTotal
        }

def SPWithOutputParametersDemo(request):
    cnxn = GetConnection()
    cursor = cnxn.cursor()
    count = 0
    cursor.execute("{call USP_GetOrdersCount(?)}", count)
    count = cursor.fetchval()
    
    cursor.execute("{call USP_GetAllOrders}")
    orders = cursor.fetchall()
    
    return render(request, 'dbfa/ShowOrders.html', {'Orders': orders, 'Count': count})

def GetConnection():
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;Server=.;Database=Northwind;Trusted_Connection=YES;')
    return (conn)


def FilteringQuerySetsDemo(request):
    # orders = Orders.objects.all()
    
    # orders = Orders.objects.filter(freight__gt=20)
    # orders = Orders.objects.filter(freight__gte=20)
    # orders = Orders.objects.filter(freight__lt=20)
    # orders = Orders.objects.filter(freight__lte=20)
    
    # orders = Orders.objects.filter(shipcountry__exact='Germany')
    # orders = Orders.objects.filter(shipcountry__contains='land')
    # orders = Orders.objects.filter(orderid__exact=10248)
    # orders = Orders.objects.filter(employeeid__in=[1, 3, 5])
    # orders = Orders.objects.filter(employeeid__in=[1, 3, 5]).order_by('employeeid')
    # orders = Orders.objects.filter(employeeid__in=[1, 3, 5]).order_by('-employeeid')
    
    # orders = Orders.objects.filter(shipname__startswith='A')
    # orders = Orders.objects.filter(shipname__endswith='e')
    
    # orders = Orders.objects.filter(freight__range=[10, 20])
    
    # orders = Orders.objects.filter(shipname__startswith='A') | Orders.objects.filter(freight__lt=20)
    # orders = Orders.objects.filter(shipname__startswith='A') & Orders.objects.filter(freight__lt=20)
    # orders = Orders.objects.filter(Q(shipname__startswith='A') | Q(freight__lt=20))
    # orders = Orders.objects.filter(Q(shipname__startswith='A') & Q(freight__lt=20))
    # orders = Orders.objects.filter(shipname__startswith='A', freight__lt=20)
    
    
    # orders = Orders.objects.exclude(shipname__startswith='A')
    # orders = Orders.objects.filter(~Q(shipname__startswith='A'))
    
    
    # orders = Orders.objects.all().order_by('orderid')
    # orders = Orders.objects.all().order_by('-orderid')
    # orders = Orders.objects.all().order_by('shipcountry')
    
    year = 1997
    orders = Orders.objects.filter(orderdate__year=year).order_by('-orderdate', 'employeeid')
    
    avg = Orders.objects.all().aggregate(Avg('freight'))
    max = Orders.objects.all().aggregate(Max('freight'))
    min = Orders.objects.all().aggregate(Min('freight'))
    sum = Orders.objects.all().aggregate(Sum('freight'))
    count = Orders.objects.all().aggregate(Count('freight'))
    
    my_dict = {
        'Orders': orders, 
        'avg': avg['freight__avg'],
        'count': count['freight__count'],
        'sum': sum['freight__sum'],
        'min': min['freight__min'],
        'max': max['freight__max']
    }
    
    
    # print(type(orders))
    # print(str(orders.query))
    
    return render(request, 'dbfa/FilteringDemo.html', {'Orders': my_dict})


def TwoLevelAccordionDemo(request):
    orders = Orders.objects.filter(orderid__range=[10248, 102555]).order_by('orderid')
    order_ids = [order.orderid for order in orders]
    order_details_list = OrderDetails.objects.filter(orderid__in=order_ids).order_by('orderid') 
    
    return render(request, 'dbfa/OrdersWithAccordion.html', {
        'orders' : orders,
        'order_details': order_details_list
    })
    
def MultiLevelAccordionDemo(request):
     employees_list = Employees.objects.order_by('employeeid')
     order_ids = Orders.objects.filter(employeeid__in=employees_list).values_list('orderid', flat=True).distinct()
     orders = Orders.objects.filter(orderid__in=order_ids,orderid__range=[10248,10270]).order_by('orderid')
     #orders=Orders.objects.all()
     order_ids = [order.orderid for order in orders]
     print(order_ids)
     order_details_list = OrderDetails.objects.filter(orderid__in=order_ids).order_by('orderid')

     return render(request, 'dbfa/MultiLevelAccordion.html', {  
        'employees': employees_list,    
        'orders': orders,
        'order_details': order_details_list,        
    })  
