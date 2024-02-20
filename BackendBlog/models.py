from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default='')
    active = models.IntegerField()    

class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    edited = models.IntegerField(default=0)
    public = models.IntegerField(default=1)
    like = models.IntegerField(default=0)
    publish = models.CharField(max_length=50)
