from django.urls import path
from .views import Homepage

app_name='app'
urlpatterns=[
    path('',Homepage,name='home')
]