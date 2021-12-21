from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':"Username"}),
            'email':forms.TextInput(attrs={'class':'form-control','type':"email", 'name':"email", 'placeholder':"Adresse e-mail"}),
            'password':forms.TextInput(attrs={'class':'form-control','type':"password",'name':"mdp", "placeholder":"Mot de passe"}),
        }
   
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['genre', 'profil','passwordConfirm']
        widgets = {
            'genre':forms.Select(attrs={'class':'form-control','name':"profil"}),
            'profil':forms.Select(attrs={'class':'form-control','name':"profil"}),
            'passwordConfirm':forms.TextInput(attrs={'class':'form-control','type':"password",'name':"mdpConfirm", "placeholder":"Confirmation du Mot de passe"})

        }