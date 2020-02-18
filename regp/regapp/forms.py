from django import forms
from django.contrib.auth.models import User
from .models import usermodel

class userform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(),required=False)
	class Meta():
		model=User
		fields=['username','email']

