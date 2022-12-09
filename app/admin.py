from django.contrib import admin

# importing from models
from .models import *


# Register your models here.
admin.site.register(Post)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Comment)