from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    model = models.CharField(max_length=50)
    desc = models.TextField(max_length=300)
    price = models.IntegerField()
    date = models.DateField()
    img = models.ImageField(upload_to = 'media',default='Product Image')

    def __str__(self):
        return self.name
class Contact(models.Model):
    name =models.CharField(max_length=120)
    email =models.EmailField(max_length=40)
    desc =models.TextField(max_length=500)    