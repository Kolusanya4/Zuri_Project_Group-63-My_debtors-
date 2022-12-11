from django.urls import path
from .views import Register,VerifyEmail,Login, PostView, PostDetailView, CreatePost, UpdatePost, DeletePost, AddCommentView

urlpatterns=[
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('verify-email/',VerifyEmail,name='verify'),
    path('post/', PostView.as_view(), name='post'),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/edit/<int:pk>',UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>/remove',DeletePost.as_view(), name='delete_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]