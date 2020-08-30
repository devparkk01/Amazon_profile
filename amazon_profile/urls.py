"""amazon_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_profile import views as profile_views 

urlpatterns = [
    path('admin/', admin.site.urls ) ,
    path('' , profile_views.home , name = "home_page") , 
    path('register/' , profile_views.register , name = "register" ) ,
    path('logout/' , profile_views.logout_view , name = 'logout' ) ,
    path('apply/' , profile_views.apply , name = "apply_page" ) , 
    path('login/' , profile_views.login_view , name = "login") , 
    path('edit_profile' , profile_views.edit_profile , name = "edit_profile") , 
    path('update_password/' , profile_views.update_password , name = "update_password") , 
]
