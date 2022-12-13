from django.urls import path
from .views import Register,VerifyEmail,Login,DashBoard,CreatePost,Logout

urlpatterns=[
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('verify-email/',VerifyEmail,name='verify'),
    path('user/dashboard',DashBoard,name='dashboard'),
    path('user/post',CreatePost,name='post')
]