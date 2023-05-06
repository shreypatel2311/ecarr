from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import transaction
from .models import User
class AdminRegisterForm(UserCreationForm):
    class  Meta(UserCreationForm.Meta):
        model = User
        fields =('username','email','password1','password2','is_admin','is_user')


    @transaction.atomic
    def save(self):
        User = super().save(commit= False)
        User.is_admin = True
        User.save()
        return User
    

class UserRegisterForm(UserCreationForm):
    class  Meta(UserCreationForm.Meta):
        model = User
        fields =('username','email','password1','password2','city','state')


    @transaction.atomic
    def save(self):
        User = super().save(commit= False)
        User.is_user = True
        User.save()
        return User
    
