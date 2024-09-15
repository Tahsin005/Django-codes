from django.db import models

# Create your models here.
class Authors(models.Model):
    AuthorName = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    BookName = models.CharField(max_length=100)

    # Optional: Custom initializer
    def custom_init(self, AuthorName, Country, BookName):
        self.AuthorName = AuthorName
        self.Country = Country
        self.BookName = BookName

    def __str__(self):
        return self.AuthorName
        
        