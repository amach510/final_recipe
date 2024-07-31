from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='users', default='no_picture.jpg')
    bio = models.TextField(help_text="No bio ...", null=True, blank=True)


    def __str__(self):
        return f"{self.name}"
