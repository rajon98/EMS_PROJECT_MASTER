from django import forms
from django.contrib.auth.models import User
from . import models 
from django.contrib.admin.widgets import AdminDateWidget


class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class EventCategoryForm(forms.ModelForm):
    class Meta:
        model=models.EventCategory
        fields=['name','code','status']
   

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
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
            'password':forms.PasswordInput()
        }

class AttendeeForm(forms.ModelForm):
    class Meta:
        model=models.Attendee
        fields=['gender','image','dob','contact','address','profesion','last_education']
        widgets={
            'dob':AdminDateWidget()
        }
       

       
   