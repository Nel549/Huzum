from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Message(models.Model):
    msg = models.TextField()


    def __str__(self):
        return self.msg
