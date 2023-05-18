from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='author')
    registered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


