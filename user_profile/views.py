from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout , update_session_auth_hash
from django.contrib import messages 
from .forms import UserRegisterForm , UserAuthenticationForm, UserChangeForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required 


# # Create your views here.

def home (request ) :
    return render (request, 'user_profile/home.html')

def register (request ) :
    if(request.method == "POST") :
        form =  UserRegisterForm(request.POST) 
        if form.is_valid() :
            form.save()
            email = form.cleaned_data.get("email")
            rawpassword = form.cleaned_data.get('password1')
            user = authenticate(request , email = email , password = rawpassword)
            
            login(request , user ) 
            messages.success(request , f"Account created for {email}")
            return redirect('home_page')
        else :
            return render(request  , 'user_profile/register.html' , {'form' : form}) 

    form = UserRegisterForm() 
    return render(request , 'user_profile/register.html' , {'form' :  form })

    
def login_view (request ) :
    if request.method == "POST" :
        login_form = UserAuthenticationForm(request.POST) 
        if login_form.is_valid() :
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request , email = email , password = password)
            if user  : 
                login(request , user = user ) 
                messages.info(request , f"Hello  {email} ")
                return redirect('home_page')
            else :
                messages.error(request , f"Invalid Login")
    else : 
        login_form = UserAuthenticationForm()
    return render(request , 'user_profile/login.html' , {"login_form"  : login_form } )
   
def logout_view (request) :
    logout(request ) 
    return redirect('home_page')

@login_required(login_url= 'login')
def edit_profile (request ) :
    if request.method == "POST" :
        form = UserChangeForm(request.POST , instance= request.user) 
        if form.is_valid() :
            form.save() 
            return redirect('home_page')
    
    else :
        form = UserChangeForm(instance= request.user)
    return render (request , 'user_profile/edit_profile.html' , {'form' : form })


@login_required (login_url= "login")
def apply(request ) :
    return render(request , 'user_profile/apply.html' , { }) 


@login_required(login_url= "login")
def update_password (request ) :
    if request.method == "POST" :
        form = PasswordChangeForm(data = request.POST , user= request.user )
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request , form.user)
            return redirect('home_page')

    
    else : 
        form = PasswordChangeForm(user = request.user )
    
    return render(request , 'user_profile/edit_password.html' , {"form" : form }) 


