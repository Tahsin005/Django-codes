from django.db import models

# Create your models here.
class Department(models.Model):
    DeptName = models.CharField(max_length=30)
    LocationName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.DeptName
    
class Country(models.Model):
    CountryName = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.CountryName
    
class Employee(models.Model):
    COUNTRIES = [
        ('BAN', 'Bangladesh'),
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('CAN', 'Canada')  ,
        ('AUS', 'Australia'),
        ('JPN', 'Japan'),
    ]
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    TitleName = models.CharField(max_length=100)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    BirthDate = models.DateField()
    HireDate = models.DateField()
    Notes = models.CharField(max_length=200)
    # Country = models.CharField(max_length=100, choices=COUNTRIES, default=None)
    Email = models.EmailField(default="", max_length=50)
    PhoneNumber = models.CharField(default="", max_length=100)
    EmpDepartment = models.ForeignKey("Department", default=0, on_delete=models.PROTECT, related_name="Departments")
    EmpCountry = models.ForeignKey("Country", default=0, on_delete=models.PROTECT, related_name="Countries")
    
class PartTimeEmployee(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    TitleName = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.FirstName} {self.LastName} - {self.TitleName}'


class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None) 
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return self.name
    
class OnSiteEmployees(models.Model):
    first_name = models.CharField(max_length=30 , null=True)
    last_name = models.CharField(max_length=30 , null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name