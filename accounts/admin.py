from django.contrib import admin
from .models import SchoolOwner, Post, Comment


# Register your models here.
admin.site.register(SchoolOwner)
admin.site.register(Post)
admin.site.register(Comment)