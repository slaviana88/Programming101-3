from django.db import models
# Create your models here.

class Container(models.Model):
    name_container = models.CharField(max_length=50)
    name_owner = models.CharField(max_length=50)
    ssh_key = models.CharField(max_length=200)
