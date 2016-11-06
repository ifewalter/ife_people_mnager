__author__ = 'ife'

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.TextField(max_length=100)
    email_address = models.EmailField(max_length=254)