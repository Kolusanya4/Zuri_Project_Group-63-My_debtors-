from django.urls import path
from .views import Register,VerifyEmail,Login,DashBoard,ViewPost,Logout,CreatePost,DeletePost,CreateComment,ViewComments,CreateContend,ContendList

urlpatterns=[
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('verify-email/',VerifyEmail,name='verify'),
    path('user/dashboard',DashBoard,name='dashboard'),
    path('user/posts',ViewPost,name='post'),
    path('delete/<id>',DeletePost,name='delete'),
    path('user/create-post',CreatePost,name='create-post'),
    path('user/comment/<id>',CreateComment,name='comment'),
    path('user/view-comment/<id>',ViewComments,name='viewcom'),
    path('user/create-contend/<id>',CreateContend,name='contend'),
    path('user/contends-list',ContendList,name='listcontend')
    

]