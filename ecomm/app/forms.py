from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm, UsernameField
from django.contrib.auth.models import User

from . models import Customer, Comment

#for login form 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus ':'True', 'class':'form-control'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))



#for registration form 
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True', 'class':'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget = forms.PasswordInput(attrs= {'autofocus':'True','autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget = forms.PasswordInput(attrs= {'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs= {'autocomplete':'current-password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordChangeForm):
    pass

class CustomerProfileForm(forms.ModelForm):
   class Meta:
        model = Customer
        fields = ['firstname','lastname', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'firstname':forms.TextInput(attrs = {'class':'form-control'}),
            'lastname':forms.TextInput(attrs = {'class':'form-control'}),
            'city':forms.TextInput(attrs = {'class':'form-control'}),
            'mobile':forms.NumberInput(attrs = {'class':'form-control'}),
            'state':forms.Select(attrs = {'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs = {'class':'form-control'}),
        }



class CommentForm(forms.ModelForm):
  
        comment = forms.CharField(
        label="Your Comment",
        widget=forms.Textarea(attrs={
            'class': 'form-control',  
            'placeholder': 'Write your comment here...',
            'rows': 4,  # Number of visible lines
            'cols': 50  # Number of visible columns (optional)
        }))
        class Meta:
            model = Comment
            fields = ['comment']
 

