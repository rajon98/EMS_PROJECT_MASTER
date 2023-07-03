from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image

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
    name=models.CharField(max_length=100)
    image=models.ImageField(blank=True)
    contact=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=genders,default='male')
    dob=models.DateField(null=False)
    profesion=models.CharField(max_length=100)
    last_education=models.CharField(max_length=100)

    def save(self,*args,**kwargs):
         super().save()
         img=Image.open(self.image.path)
         if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)

