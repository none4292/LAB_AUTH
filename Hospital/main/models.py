from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=1024)
    pcontent = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="img/blog/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"{self.title} "


class Appointment(models.Model):

    fullname =models.CharField(max_length=1024)
    email = models.EmailField()
    number = models.IntegerField()
    department = models.TextField()
    message = models.TextField()
    date = models.DateTimeField()





class Contact(models.Model):

    name = models.CharField(max_length=1024)
    email = models.EmailField()
    subject=models.CharField(max_length=500)
    content = models.TextField()




class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1024)
