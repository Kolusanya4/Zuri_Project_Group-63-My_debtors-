# from django.db import models
# import email #for email field
# from django.contrib.auth.models import User

# # Create your models here.
# class Post(models.Model):

#     STATUS = (
#         ('Active', 'Active'),
#         ('Pending', 'Pending'),
#         ('Resolved', 'Resolved'),
#     )
#     post_name = models.CharField(max_length=100)
#     post_email = models.EmailField()
#     post_phone = models.IntegerField()
#     post_debt = models.IntegerField()
#     post_paid_amt = models.IntegerField()
#     post_status = models.CharField(max_length=60, choices=STATUS, default='Active')
#     post_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.post_name +' '+ self.post_date

# class School(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name_of_school = models.CharField(max_length=150)
#     post_school = models.ForeignKey(Post, max_length=150, on_delete=models.CASCADE)
#     school_email_address = models.EmailField()
#     location_of_school = models.CharField(max_length=150)
#     school_phone = models.IntegerField()

#     def __str__(self):
#         return self.name_of_school


# class Student(models.Model):
#     student_school = models.ForeignKey(School, on_delete=models.CASCADE)
#     student_firstname = models.CharField(max_length=100)
#     student_lastname = models.CharField(max_length=150)
#     student_email = models.EmailField()
#     student_phone = models.IntegerField()

#     def __str__(self):
#         return self.student_firstname +' '+ self.student_lastname

# class Comment(models.Model):
#     comment_post = models.ForeignKey(Post, max_length=150, on_delete=models.CASCADE)
#     Comment_name = models.CharField(max_length=100)
#     Comment_body = models.TextField(max_length=500)
#     comment_date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.Comment_name +' '+ self.comment_date_created


