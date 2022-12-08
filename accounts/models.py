from django.db import models

# Create your models here.
class SchoolOwner(models.Model):
    fullname=models.CharField(max_length=600)
    # logo=models.ImageField(null=True,blank=True)
