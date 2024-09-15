from django.db import models

# Create your models here.
class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    production_year = models.CharField(max_length=255)
    car_body = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.car_brand}'