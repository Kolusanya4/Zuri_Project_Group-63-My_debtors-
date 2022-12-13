from django.contrib import admin
from .models import School,Debtor,DebtInfo
# Register your models here.
admin.site.register(School)
admin.site.register(Debtor)
admin.site.register(DebtInfo)
