from django.urls import path
from .views import Homepage,Faq,Contact

app_name='app'
urlpatterns=[
    path('',Homepage,name='home'),
    path('faqs/',Faq,name='faq'),
    path('contact-us',Contact,name='contact')
]