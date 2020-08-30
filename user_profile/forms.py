from django import forms
from .models import MyUser

class UserRegisterForm (forms.ModelForm) :
    password1 = forms.CharField(label = "Password " , widget = forms.PasswordInput )
    password2 = forms.CharField(label = "Password Confirmation " ,widget = forms.PasswordInput)

    class Meta : 
        model = MyUser 
        fields = ('email' , 'username' , 'firstname','password1' , 'password2' )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_username(self) :
        username = self.cleaned_data.get('username')
        qs = MyUser.objects.filter(username = username )
        if qs.exists() : 
            raise forms.ValidationError("Username is taken")
        return username 
    
    def clean_password2 (self ) :
        # Check that the two password entries match 
        password1 = self.cleaned_data.get('password1') 
        password2 = self.cleaned_data.get('password2') 

        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("Two passwords do not match ")
        return password2 
    
    

    def save( self , commit = True) :
        #  save the provided password in hashed format 
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password1"]) 

        if commit :
            user.save() 
        return user 



class UserChangeForm(forms.ModelForm):
    """A form for updating users. """

    class Meta:
        model = MyUser
        fields = ('email' , 'username' , 'firstname')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = MyUser.objects.filter(email=email)
    #     if qs.exists() and request.user != qs :
    #         raise forms.ValidationError("Email is taken")
    #     return email
    
    # def clean_username(self) :
    #     username = self.cleaned_data.get('username')
    #     qs = MyUser.objects.filter(username = username )
    #     if qs.exists() : 
    #         raise forms.ValidationError("Username is taken")
    #     return username 



class UserAuthenticationForm(forms.Form) :
    email    = forms.EmailField(label = "Email"  )
    password = forms.CharField(label = "Password " , widget = forms.PasswordInput)

    def clean_email(self ) :
        # if self.is_valid() :
        email = self.cleaned_data.get('email') 
        qs = MyUser.objects.filter(email = email ) 
        if not qs.exists()  : 
            raise forms.ValidationError("Not registered ")
        return email 




