from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser 
from django.contrib.auth.models import Group 
from .forms import UserRegisterForm 
# Register your models here.


class MyUserAdmin (BaseUserAdmin) :
    # The form to add user instances
    add_form = UserRegisterForm

    list_display = ('email' , 'username' ,'firstname' ,
    'date_joined' ,'last_login' , 'is_admin', 'is_staff')

    search_fields = ('email' , 'username')

    readonly_fields = ('date_joined' , 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'username' , 'password')}),
        ('Personal info', {'fields': ('firstname',)}),
        ('Permissions', {'fields': ('is_admin','is_active', 'is_staff' , 'is_superuser')}),
    )

    filter_horizontal = () 
    list_filter = ()



admin.site.register(MyUser , MyUserAdmin)
admin.site.unregister(Group)
# since we're not using Django's built-in permissions, unregister the Group model from admin.