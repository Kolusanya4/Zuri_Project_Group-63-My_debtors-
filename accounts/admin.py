from django.contrib import admin
from .models import School,Debtor,Post,Comment
# Register your models here.

admin.site.register(School)
admin.site.register(Debtor)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created',]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)