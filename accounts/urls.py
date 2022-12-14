from django.urls import path
from .views import Register,VerifyEmail,Login,DashBoard,ViewPost,Logout,CreatePost,DeletePost

urlpatterns=[
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('verify-email/',VerifyEmail,name='verify'),
    path('user/dashboard',DashBoard,name='dashboard'),
    path('user/posts',ViewPost,name='post'),
    path('user/create-post',CreatePost,name='create-post'),
    path('user/delete-post/<int:id>',DeletePost,name='delete')
]