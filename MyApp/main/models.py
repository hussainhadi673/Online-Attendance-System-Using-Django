from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):
    name1 = models.CharField(max_length=50)
    username1= models.CharField(max_length=50)
    date1 = models.CharField(max_length=50)
    attendance2 = models.CharField(max_length=50)

    object = models.Manager()

    def __str__(self):
        return f'{self.username1}  {self.date1}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Leave_Request(models.Model):
    name2 = models.CharField(max_length=50)
    username2 = models.CharField(max_length=50)
    date2 = models.CharField(max_length=50)
    concern = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.username2}  Leave Request'