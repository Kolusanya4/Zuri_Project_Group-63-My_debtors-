from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import CreateUserForm,SchoolForms,DebtorForms,DebtorInfoForm,ContendForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Post,School,Debtor,Comment,Contend
from django.contrib.auth.models import Group
from .decorators import allowed_user
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        form=CreateUserForm(data=request.POST)
        profile=SchoolForms(data=request.POST)
        debtor=DebtorForms(data=request.POST)
        if form.is_valid() and profile.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            school_group=Group.objects.get(name='Schoolowners')
            user.groups.add(school_group)
            user.save()
            user_profile=profile.save(commit=False)
            user_profile.user=user
            user_profile.save()
            return redirect('verify')
        elif form.is_valid() and debtor.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            debtor_group=Group.objects.get(name='Debtors')
            user.groups.add(debtor_group)
            user.save()
            debt_profile=debtor.save(commit=False)
            debt_profile.user=user
            debt_profile.save()
            return redirect('verify')
    form=CreateUserForm()
    profile=SchoolForms()
    debtor=DebtorForms()
    return render(request,'register.html',{'form':form,'schoolform':profile,'debtorform':debtor})
@csrf_exempt
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
    return render(request,'verification1.html')

@csrf_exempt
def Login(request):

    
    if request.user.is_authenticated:
        return redirect('dashboard')

    elif request.method=='POST':
        uname=request.POST.get('username')
        pw=request.POST.get('password')
        user=authenticate(username=uname,password=pw)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Wrong login credentials')
    return render(request,'login.html')
@csrf_exempt
@login_required(login_url='login')
def DashBoard(request):
    if request.user.groups.filter(name='Schoolowners').exists():
        school_owner=School.objects.filter(user=request.user)[0]
        debt_info=Post.objects.filter(Author=school_owner)
        
        return render(request,'dashboard.html',{'infos':debt_info,'school':school_owner})
    elif request.user.groups.filter(name='Debtors').exists():
        debtor=Debtor.objects.filter(user=request.user)
        return redirect('post')
@csrf_exempt
@login_required(login_url='login')
def ViewPost(request):    
        debtpost=Post.objects.all().order_by('created')
        check_create=request.user.groups.filter(name='Schoolowners').exists()
        if check_create:
            school_owner=School.objects.filter(user=request.user)[0]
            return render(request,'post.html',{'check':check_create,'debts':debtpost,'school':school_owner})
        elif request.user.groups.filter(name='Debtors').exists():
           debtor=Debtor.objects.filter(user=request.user)[0]
           return render(request,'post.html',{'check':check_create,'debts':debtpost,'debtor':debtor})


@csrf_exempt
@login_required(login_url='login')
def CreatePost(request):
        school_name=School.objects.filter(user=request.user)[0]
        if request.method=='POST':
            form=DebtorInfoForm(data=request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.Author=school_name
                instance.save()
                return redirect('dashboard')
        else:
                 form=DebtorInfoForm()
                 return render(request,'createpost.html',{'form':form})

@csrf_exempt
@login_required(login_url='login')
def DeletePost(request,id):
    post_item=Post.objects.get(id=id)
    post_item.delete()
    return redirect('dashboard')

@csrf_exempt
@login_required(login_url='login')
def Logout(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('login')

@csrf_exempt
@login_required(login_url='login')
def CreateComment(request,id):
    post_instance=Post.objects.get(id=id)
    if request.method=='POST':
        comment_instance=Comment.objects.create(
            author=request.user,
            post=post_instance,
            content=request.POST['comment']
        )
        comment_instance.save()
        return redirect('post')
    return redirect('post')

@csrf_exempt
@login_required(login_url='login')
def ViewComments(request,id):
        post_instance=Post.objects.get(id=id)
        comments=Comment.objects.filter(post=post_instance)
        debtpost=Post.objects.all().order_by('created')
        
        check_create=request.user.groups.filter(name='Schoolowners').exists()
        if check_create:
            school_owner=School.objects.filter(user=request.user)[0]
            return render(request,'comments.html',{'check':check_create,'debts':debtpost,'school':school_owner,'comments':comments,})
        elif request.user.groups.filter(name='Debtors').exists():
           debtor=Debtor.objects.filter(user=request.user)[0]
           return render(request,'comments.html',{'check':check_create,'debts':debtpost,'debtor':debtor,'comments':comments,})

@csrf_exempt
@login_required(login_url='login')
def CreateContend(request,id):
    post_instance=Post.objects.get(id=id)
    if request.method=='POST':
        form=ContendForm(data=request.POST)
        if form.is_valid:
            contend=form.save(commit=False)
            contend.post=post_instance
            contend.author=request.user
            contend.save()
            return redirect('post')
    form=ContendForm()
    return render(request,'createcontend.html',{'form':form})

@csrf_exempt
@login_required(login_url='login')
def ContendList(request):

    check_create=request.user.groups.filter(name='Schoolowners').exists()
    school_instance=School.objects.filter(user=request.user)
    contends_made=None
    post_contented=Post.objects.filter(Author=school_instance[0])
    if post_contented:
        contends_made=Contend.objects.filter(post=post_contented[0])
    debtor=None
    if contends_made:
        debtor=Debtor.objects.filter(user=contends_made[0].author)[0].guardian_name
    
    return render(request,'contendlist.html',{'contends':contends_made,'check':check_create,'school':school_instance[0],'debtor':debtor})


