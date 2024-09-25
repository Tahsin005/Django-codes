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
    return render(request, 'dbfa/ShowOrders.html', {'Orders': orders})

def StoredProcedureDemo(request):
    cnxn = GetConnection()
    cursor = cnxn.cursor()
    cursor.execute("{call USP_GetAllOrders}")
    orders = cursor.fetchall()
    return render(request, 'dbfa/ShowOrders.html', {'Orders': orders})

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