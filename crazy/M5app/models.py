from django.db import models
from django.urls import reverse

# Create your models here.
class userimg(models.Model):
    gender=(("male","male"),("female","female"))
    img=models.ImageField(upload_to='media')
    name=models.CharField(max_length=30)
    price=models.FloatField()
    species=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30,choices=gender)
    description=models.CharField(max_length=150)


class meta:
    db_tb='userimg'    
    
def get_absolute_url(self):
    return reverse('list')
