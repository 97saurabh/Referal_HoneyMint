from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators


class UserCreateForm(UserCreationForm):

    class Meta:
        fields=('username','email','password1','password2','first_name','last_name')
        model=get_user_model()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['first_name'].label = "Your First Name"
        self.fields['first_name'].label = "Your Last Name"
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
class FormName(forms.Form):
    Referal_Code=forms.CharField()
