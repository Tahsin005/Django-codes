from django.shortcuts import render
from . models import Categories
import pyodbc
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
