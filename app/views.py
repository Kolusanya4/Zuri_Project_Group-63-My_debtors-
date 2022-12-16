from django.shortcuts import render

# Create your views here.
def Homepage(request):
   return render(request,'about.html')

def Faq(request):
       return render(request,'faq.html')

def Contact(request):
   return render(request,'contactus.html')