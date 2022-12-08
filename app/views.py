from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request,'home.html')