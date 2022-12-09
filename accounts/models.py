from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SchoolOwner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    schoolname=models.CharField(max_length=600)
    phone=models.IntegerField(default=234)
    address=models.CharField(max_length=700,blank=True)
    
    def __str__(self) -> str:
        return self.schoolname
    
