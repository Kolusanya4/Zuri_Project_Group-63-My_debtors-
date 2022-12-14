from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class School(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    schoolname=models.CharField(max_length=600)
    phone=models.IntegerField(default=234)
    address=models.CharField(max_length=700,blank=True)
    is_schoolowner=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.schoolname

class Debtor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    school_name=models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    guardian_name=models.CharField(max_length=400)
    level=models.CharField(max_length=400)
    full_name=models.CharField(max_length=400)
    is_debtor=models.BooleanField(default=True) 

    def __str__(self):
        return self.guardian_name


class Post(models.Model):
    status=(
        ('Pending','pending'),
        ('Active','active'),
        ('Paid','paid')
    )
    Author=models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    debtor_name=models.CharField(max_length=500)
    debt_amount=models.CharField(max_length=500)
    debt_status=models.CharField(max_length=200, choices=status,default='Active')
    content=models.TextField(blank=True)
    created=models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created', )
    def __str__(self):
            return str(self.debtor_name)
class Comment:
    author=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,null=True,blank=True,on_delete=models.CASCADE)
    content=models.TextField(default='Add comment')
    date_created=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
         return self.author
