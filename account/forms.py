

from dataclasses import fields
from .models import Profile
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,BaseUserCreationForm,PasswordChangeForm
import random


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control'})

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control form-control-user",'placeholder':'Enter Email Address...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",'placeholder':'Password'}))
    remember_me = forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={'class':'custom-control-input'}))


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not  User.objects.filter(email=email).exists():
            self.add_error("email",'Email adresi sisteme kayitli degil')

        return email
    

class CreateUserForm(BaseUserCreationForm):
    class Meta:
        model= User
        fields = ('email','first_name','last_name',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'Password'})
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Lastname'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control form-control-user','placeholder':'Email'})

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            self.add_error('email','Email daha once kullanilmis')

        return email
    
    def save(self,commit=True):
        user = super(CreateUserForm,self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.username = '{}_{}_{}'.format(
            self.cleaned_data.get('first_name').lower(),
            self.cleaned_data.get('last_name').lower(),
            random.randint(11111,99999)
        )

        if commit:
            user.save()

        return user
    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('first_name','last_name','email')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','locations')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields['locations'].widget = widgets.TextInput(attrs={'class':'form-control'})
   