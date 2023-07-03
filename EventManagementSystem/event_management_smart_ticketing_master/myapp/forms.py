from django import forms
from django.contrib.auth.models import User
from . import models 

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class OrganizerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
            'password':forms.PasswordInput()
        }

class OrganizerForm(forms.ModelForm):
    class Meta:
        model=models.Organizer
        fields=['organization_name','organization_type','address','contact','status']

class AttendeeUserForm(forms.ModelForm):
    class Meta:
        model:User
        fields=['last_name','first_name','email','username','password']

class AttendeeForm(forms.ModelForm):
    class Meta:
        model=models.Attendee
        fields=['name','gender','image','contact','address','profesion','last_education']
   