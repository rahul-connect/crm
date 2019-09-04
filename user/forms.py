
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','role','phone','select_center')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','phone','select_center')

        widgets={
                   "username":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "last_name":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "email":forms.EmailInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "phone":forms.NumberInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "select_center":forms.Select(attrs={'class':'form-control','disabled':'disabled'}),
                }  


