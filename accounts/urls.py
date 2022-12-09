from django.urls import path
from .views import Register,VerifyEmail,Login

urlpatterns=[
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('verify-email/',VerifyEmail,name='verify')
]