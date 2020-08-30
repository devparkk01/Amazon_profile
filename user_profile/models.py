from django.db import models
from django.contrib.auth.models import (AbstractBaseUser ,
BaseUserManager )


# Creating custom manager model

class MyUserManager (BaseUserManager ) :

    def create_user(self , email , username , firstname , password = None ) :
        # create user here
        if not email :
            raise ValueError("user must have an email ")

        if not username :
            raise ValueError("user must have a username ")

        if not firstname :
            raise ValueError("user must have a first name ")

        user = self.model(email = self.normalize_email(email ),
                        username = username , 
                        firstname = firstname 
        )

        user.set_password(password) 
        user.save(using = self._db)
        return user 

    
    def create_superuser(self , email , username , firstname , password = None ) :
        # create superuser here

        user = self.create_user(email = email  , username = username,
         firstname = firstname , password = password 
        ) 

        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using = self._db)

        return user 


# Creating custom user model 
class MyUser (AbstractBaseUser) :
    email              = models.EmailField(verbose_name ="email" , max_length = 60 , unique = True  )
    username           = models.CharField(max_length =30 , unique = True ) 
    firstname          = models.CharField(max_length = 30 )
    
    # The following fields are required when we are creating a custom user model 
    date_joined        = models.DateTimeField(verbose_name= "date joined" ,auto_now_add= True)
    last_login         = models.DateTimeField(verbose_name= "last login" , auto_now= True) 
    is_admin           = models.BooleanField(default= False ) 
    is_active          = models.BooleanField(default= True)
    is_staff           = models.BooleanField(default= False)
    is_superuser       = models.BooleanField(default= False) 


    #  we need to set the USERNAME_FIELD to whatever we want the user to be able to login with 
    USERNAME_FIELD     = 'email' # since we want the user to login with `email`, therefore 
                #  set USERNAME_FIELD to email 

    REQUIRED_FIELDS    = ["username" , "firstname"] 

    objects = MyUserManager() # specify custom usermanager for this custom user


    def __str__ (self ) : 
        return self.email 
    
    #  The following methods are required when we are creating a custom user model 
    def has_perm (self , perm , obj = None ) :
        return self.is_admin 
    
    def has_module_perms (self , app_label ) : 
        return True 
    

