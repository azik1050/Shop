from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import UserReview



class AdvancedUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your username'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Confirm your password'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AdvancedAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your email'
    }))
    class Meta:
        model = User
        fields = ('username', 'email')

class UserBioForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'massage-bt',
        'placeholder': 'Enter your bio'
    }))
    class Meta:
        model = Profile
        fields = ('bio',)

class UserImgForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class UserReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter your phone'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'massage-bt',
        'placeholder': 'Enter your comment'
    }))
    class Meta:
        model = UserReview
        fields = ('name', 'email', 'phone', 'text')


