from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import CreateUserForm,SchoolForms, CommentForm, ContendForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy



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

def ContendView(request):

    form = ContendForm()
    if request.method == 'POST':
        print(request.POST)
        form = ContendForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'contend.html', context)

def ContendSuccess(request):
    return render(request, 'contend_success.html')


# list all the post from database
class PostView(ListView):
    model = Post
    posts = Post.objects.all()
    template_name = 'post.html'

#list a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

#create a post view
class CreatePost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

#update a post
class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['debt_amount', 'debt_paid_amt', 'post_status']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post')



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('post')




    

