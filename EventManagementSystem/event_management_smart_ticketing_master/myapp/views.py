from django.shortcuts import render,redirect,HttpResponse
from . import forms,models
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect


# Create your views here.

def home_view(request):
      # if request.user.is_authenticated:
      #  return HttpResponseRedirect('afterlogin')
    return render(request,'index.html')

# create views for admin user

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
    print('ia, from here where there is no ui.where are yoy from.')
    return user.groups.filter(name='ORGANIZER').exists()
def is_attendee(user):
    return user.groups.filter(name='ATTENDEE').exists()

def afterlogin_view(request):
    if is_admin(request.user):
          return HttpResponse("You logged as a admin.")
    if is_organizer(request.user): 
        return HttpResponse("you logged as organizer. ")
    if is_attendee(request.user):
        return HttpResponse("you logged as attendee. ")
    
    # create view for organizer user

def organizerclick_view(request):
        #if request.user.is_authenticated:
        #  return HttpResponseRedirect('afterlogin')
        return render(request,'organizerclick.html')

def organizer_signup_view(request):
    userForm=forms.OrganizerUserForm()
    organizerForm=forms.OrganizerForm()
    mydict={'userForm':userForm,'organizerForm':organizerForm}
    if request.method=='POST':
        userForm=forms.OrganizerUserForm(request.POST)
        organizerForm=forms.OrganizerForm(request.POST)
        if userForm.is_valid() and organizerForm.is_valid():
            user= userForm.save()
            user.set_password(user.password)
            user.save()
            organizer=organizerForm.save(commit=False)
            organizer.user=user
            organizer=organizer.save()
            my_organizer_group=Group.objects.get_or_create(name='ORGANIZER')
            my_organizer_group[0].user_set.add(user)
        return HttpResponseRedirect('organizerlogin')
    return render(request,'organizersignup.html',context=mydict)

# create view for attendee user
def attendeeclick_view(request):
    #if request.user.is_authenticated:
        #  return HttpResponseRedirect('afterlogin')
        return render(request,'attendeeclick.html')

def attendee_signup_view(request):
     





        




