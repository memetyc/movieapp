from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return render('home-page')   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')

            username1 = User.objects.get(email=email).username
            user = authenticate(username=username1,password=password)
            if user is not None:
                login(request,user)
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
                return redirect('home-page')
            else:
                form.add_error(None, 'Email yada parola hatali')
                return render(request,"account/login.html",{'form':form})
        else:
            return render(request,"account/login.html",{'form':form}) 
    form = LoginForm()
    return render(request,"account/login.html",{'form':form})


def register_request(request):
    if request.user.is_authenticated:
        return redirect('home-page')   
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = user.username
            password = form.cleaned_data.get('password1')
          
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home-page')
        else:
            form.add_error(None,'Formu eksiksiz doldurmalisiniz')
            return render(request,"account/register.html",{'form':form})

    form = CreateUserForm()
    return render(request,"account/register.html",{'form':form})



def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user,request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Sifre basariyla degistirildi')
            return redirect('profile')
        else:
            return render(request,"account/change_password.html",{
                'form':form
            })

    form = UserPasswordChangeForm(request.user)
    return render(request,"account/change_password.html",{
        'form':form
    })

@login_required(login_url='/account/login')
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance = request.user)
        profile_form = ProfileForm(request.POST,instance = request.user.profile,files = request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profil bilgileriniz guncellendi')
            return redirect('profile')
        else:
            messages.error(request,'Lutfen bilgilerinizi kontrol ediniz')
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)
    return render(request,"account/profile.html",{
        'user_form':user_form,
        'profile_form':profile_form
    })


def watch_list(request):
    return render(request,"account/watch_list.html")


def logut_request(request):
    logout(request)
    return redirect('home-page')