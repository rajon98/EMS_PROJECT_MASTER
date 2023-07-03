from django.shortcuts import render,redirect,HttpResponse
from . import forms,models
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect


# Create your views here.

def home_view(request):
      # if request.user.is_authenticated:
      #  return HttpResponseRedirect('afterlogin')
    return render(request,'index.html')

def adminclick_view(request):
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('afterlogin')
    return render(request,'adminclick.html')

def admin_signup_view(request):
    form=forms.AdminSignupForm()
    if request.method=='POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            admin_user_group=Group.objects.get_or_create(name='ADMIN')
            admin_user_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_organizer(user):
    return user.groups.filter(name='ORGANIZER').exists()
def is_attendee(user):
    return user.groups.filter(name='ATTENDEE').exists()
def afterlogin_view(request):
    if is_admin(request.user):
          return HttpResponse("You logged as a admin !!")
    



        




