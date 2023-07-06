from django.shortcuts import render,redirect,HttpResponse
from . import forms,models
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

def admin_dashboard_view(request):
    return render(request,'admindashboard.html')

@login_required(login_url='adminlogin')
def event_category_create_view(request):
    form=forms.EventCategoryForm()
    if request.method=='POST':
        form=forms.EventCategoryForm(request.POST)
        if form.is_valid():
            print(request.POST['name'])
            new_user = form.save(commit=False)
            new_user.created_user = request.user
            new_user.updated_user = request.user
            new_user.save()                
    return render(request,'eventcategory.html',{'form':form})

def event_category_list_view(request):
    eventcategory=models.EventCategory.objects.all()
    return render(request,'eventcategorylist.html',{'eventcategory':eventcategory})




def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_organizer(user):
    return user.groups.filter(name='ORGANIZER').exists()
def is_attendee(user):
    if(user.groups.filter(name='ATTENDEE').exists()):
        print('ia, from here where there is no ui.where are yoy from.')
    print("iam from nowhere")
    return user.groups.filter(name='ATTENDEE').exists()

def afterlogin_view(request):
    if is_admin(request.user):
          return redirect('admin-dashboard')
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
    
    userForm=forms.AttendeeUserForm()
    attendeeForm=forms.AttendeeForm()
    mydict={'userForm':userForm,'attendeeForm':attendeeForm}
    if request.method=='POST':     
        userName=request.POST['username']   
        if User.objects.filter(username=userName).exists():
            messages.success(request,"User name already exist.please try another one.")
            alert=True
            mydict={'userForm':userForm,'attendeeForm':attendeeForm,'alert':alert}
            return render(request,'attendeesignup.html',context=mydict)
        else:
            userForm=forms.AttendeeUserForm(request.POST)
            attendeeForm=forms.AttendeeForm(request.POST,request.FILES)
            if userForm.is_valid() and attendeeForm.is_valid():
                user=userForm.save()
                user.set_password(user.password)
                group = Group.objects.get(name='ATTENDEE')
                user.groups.add(group)
                user.save()
                attendee=attendeeForm.save(commit=False)
                attendee.user=user
                attendee=attendee.save()

                user = User.objects.get(username=user.username)
                group = Group.objects.get(name="ATTENDEE")
                user.groups.add(group)
                user.save()
                return HttpResponseRedirect('attendeelogin')
      
          #  my_attendee_group=Group.objects.get_or_create(name='ATTENDEE')
         #   my_attendee_group[0].user_set.add(user)
    return render(request,'attendeesignup.html',context=mydict)
          
     





        




