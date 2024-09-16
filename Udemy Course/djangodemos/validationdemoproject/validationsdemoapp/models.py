from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
# Create your models here.
class UserRegistration(models.Model):
    # username = models.CharField(max_length=15, verbose_name="User Name")
    username = models.CharField(max_length=15, verbose_name="User Name", validators=[MinLengthValidator(5)])
    # password = models.CharField(max_length=15, verbose_name="Password")
    password = models.CharField(max_length=15, verbose_name="Password", validators=[MinLengthValidator(5)])
    # confirm_password = models.CharField(max_length=15, verbose_name="Confirm Password")
    confirm_password = models.CharField(max_length=15, verbose_name="Confirm Password", validators=[MinLengthValidator(5)])
    
    gender = models.CharField(max_length=10, verbose_name="Gender")
    country = models.CharField(max_length=20, verbose_name="Country")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    
    email = models.EmailField(verbose_name="Email")
    # postal_code = models.IntegerField(verbose_name="Postal Code")
    postal_code = models.IntegerField(verbose_name="Postal Code", validators=[MinValueValidator(1000), MaxValueValidator(9999999)])
    phone_number = models.CharField(max_length=13, verbose_name="Phone Number")
    
    profile = models.TextField(verbose_name="Profile of User", blank=True)
    website_url = models.URLField(verbose_name="Website URL")
    terms_conditions = models.BooleanField(verbose_name="Terms & Conditions")
    favwebsite_url = models.CharField(max_length=256)