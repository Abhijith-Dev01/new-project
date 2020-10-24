from django.db import models

# Create your models here.
class destination(models.Model):
    image=models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc=models.TextField()
    price = models.IntegerField(default=50)
    offer=models.BooleanField(default=False)