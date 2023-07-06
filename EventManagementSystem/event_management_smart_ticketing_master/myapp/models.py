from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

genders=[('male','male'),('frmale','female')]

class Organizer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    organization_name=models.CharField(max_length=100)
    organization_type=models.CharField(max_length=120)
    address=models.CharField(max_length=125)
    contact=models.CharField(max_length=30)
    status=models.BooleanField(default=False)

class Attendee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',blank=True)
    contact=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=genders,default='male')
    dob=models.DateField(null=True)
    profesion=models.CharField(max_length=100)
    last_education=models.CharField(max_length=100)


    def save(self,*args,**kwargs):
        super().save()
        img=Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
          new_img = (100, 100)
          img.thumbnail(new_img)
          img.save(self.image.path)

class EventCategory(models.Model):
    name=models.CharField(max_length=150,unique=True)
    code=models.CharField(max_length=6,unique=True)
    # priority=models.IntegerField(unique=True)
    created_user=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='created_user')
    updated_user=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='updated_user')
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now_add=True)
    status_choice=(('disabled','Disabled'),
                   ('active','Active'),
                   ('deleted','deleted'),
                   ('blocked','Blocked'),
                   ('completed','Completed'),)
    status=models.CharField(choices=status_choice,max_length=15,default=False)

    def __str__(self):
        return self.name


