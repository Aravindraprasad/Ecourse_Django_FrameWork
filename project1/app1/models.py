from django.db import models

# Create your models here.

class Details(models.Model):
    type = models.CharField(max_length=50,default='',null=False)
    name = models.CharField(max_length=50,default='',null=False)
    college = models.CharField(max_length=50,default='',null=False)
    branch = models.CharField(max_length=50,default='',null=False)
    year = models.CharField(max_length=50,default='',null=False)
   