from django import forms
from django.forms import ModelForm

class getRegister(forms.Form):



    email = forms.EmailField(label='Email:',max_length=254)
    name = forms.CharField(label='Name:',max_length=50)
    last_name = forms.CharField(label='Last name:',max_length=50)
    pass1 = forms.CharField(max_length=50)
    pass2 = forms.CharField(max_length=50)
    numberID = forms.IntegerField(label='Number identification')
    #photo = forms.ImageField()
