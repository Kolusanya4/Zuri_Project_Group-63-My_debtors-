from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import email

# Create your models here.
class SchoolOwner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    schoolname=models.CharField(max_length=600)
    phone=models.IntegerField(default=234)
    address=models.CharField(max_length=700,blank=True)
    
    def __str__(self) -> str:
        return self.schoolname
    
class Post(models.Model):

    STATUS = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    )
    school_owner = models.ForeignKey(SchoolOwner, on_delete=models.CASCADE, max_length=100)
    debtors_name = models.CharField(max_length=100)
    debtors_text = models.CharField(max_length=1000, default=True)
    debt_amount = models.IntegerField()
    debt_paid_amt = models.IntegerField()
    post_status = models.CharField(max_length=60, choices=STATUS, default='Active')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.debtors_name + ' ' + str(self.school_owner)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))



#comments for post
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", max_length=150, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contend(models.Model):
    post = models.OneToOneField(Post, max_length=100, on_delete = models.CASCADE )
    name = models.CharField(max_length = 100)
    email = models.EmailField(default='abc@gmail.com')
    text = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name