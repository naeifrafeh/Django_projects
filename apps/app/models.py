from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import re
import bcrypt
from datetime import date, datetime
from time import strptime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
password_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class UserManager(models.Manager):
    def register(self,request):
        if len(request.POST['name']) < 1 :
             messages.add_message(request,messages.ERROR, 'this is invalid name ')
        if len(request.POST['alias']) < 1 :
             messages.add_message(request,messages.ERROR, 'this is invalid elias ')
        if len(request.POST['email']) < 1:
            messages.add_message(request,messages.ERROR, 'email can not be empty ')
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request,messages.ERROR, 'email must match format ')
        if len(request.POST['password'])< 8:
            messages.add_message(request,messages.ERROR, 'passwprd must be between 8 to 32  ')
        if not password_REGEX.match(request.POST['password']):
            messages.add_message(request,messages.ERROR, 'password must match format ')
        if request.POST['password'] != request.POST['password_confirm'] :
            messages.add_message(request,messages.ERROR, 'password much match confirm password  ')
        if User.objects.filter(email=request.POST['email']).count() >0:
            messages.add_message(request,messages.ERROR, 'user with this email is already exist')
        # if str(date.today()) > str(request['dob']):
        #     messages.add_message(request,messages.ERROR, 'please correct the date ')
        if len(get_messages(request)) >0:
            return False
        else:
            User.objects.create(
                name=request.POST['name'],
                alias=request.POST['alias'],
                email=request.POST['email'],
                dob = request.POST['dob'],

                password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            )
            return True
    def login(self, request):
        try:
            user = User.objects.get(email=request.POST['email'])
            user.save()
          
            request.session['userId']

            isvalid = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())
            if isvalid:
                request.session['userId']= user.id
                return True
            else :
                messages.add_message(request,messages.ERROR, "Invalid Credunthial")
                return False


        except:
             messages.add_message(request,messages.ERROR, 'user does not exist')
             return False

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    friends = models.ManyToManyField('User', related_name="users_friended")    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

