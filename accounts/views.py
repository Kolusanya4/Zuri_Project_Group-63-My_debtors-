from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import CreateUserForm,SchoolForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def Register(request):
    if request.method=='POST':
        form=CreateUserForm(data=request.POST)
        profile=SchoolForms(data=request.POST)
        if form.is_valid() and profile.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            user.save()
            user_profile=profile.save(commit=False)
            user_profile.user=user
            user_profile.save()
            return redirect('verify')
    form=CreateUserForm()
    profile=SchoolForms()
    return render(request,'register.html',{'form':form,'schoolform':profile})

def VerifyEmail(request):
    if request.method=='POST':
        email_address=request.POST.get('email')
        test_user=User.objects.filter(email=email_address).exists()
        if test_user:
            user=User.objects.filter(email=email_address)[0]
            if user.is_active:
                messages.success(request,'Email already verified')
                return redirect('login')
            else:   
                user.is_active=True
                user.save()
                print(user.is_active)
                messages.success(request,'email verified successfully')
                return redirect('login')
        else:
            messages.error(request,'Email does not exist')
            return redirect('verify')
    return render(request,'verification.html')


def Login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pw=request.POST.get('password')
        user=authenticate(request,username=uname,password=pw)
        if user:
            login(request,user)
            return redirect('app:home')
        else:
            messages.error(request,'Wrong login credentials')
    return render(request,'login.html')

