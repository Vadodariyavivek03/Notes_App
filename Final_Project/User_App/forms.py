from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields='__all__'

class NotesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['title','desc','subject','notes_file']

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'


class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(required=False)
    class Meta:
        model = UserSignup
        fields = ['fullname', 'mobile', 'profile_image', 'password']
