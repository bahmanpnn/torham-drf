from django.db import models
from datetime import datetime


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
