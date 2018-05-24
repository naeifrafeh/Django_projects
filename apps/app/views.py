# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import User
from time import gmtime, strftime
from django.contrib import messages
from django.contrib.messages import get_messages
import bcrypt
import datetime

def index(request):
    return render(request,'app/index.html')

def register(request):
	if request.method == "POST":
		User.objects.register(request)
		return redirect("/")
	else:
		return redirect("/")

def login(request):
	if User.objects.login(request):
		return redirect('/home')
	else:
		return redirect('/')
		
def home(request):
    current_user = User.objects.get(id=request.session['userId'])
    friends = User.objects.filter(friends = current_user) | User.objects.filter(users_friended = current_user)
    other_people = User.objects.exclude(friends = current_user).exclude(users_friended = current_user)
    context={
        'friends':friends,
        'other_people':other_people,
        'current_user':current_user
        
    }
    return render(request,'app/home.html',context)


def logout(request):
    if 'id' not in request.session:
        return redirect('/')
    del request.session['id']
    return redirect('/')

def show_other(request, id):
    try:
       user = User.objects.get(id=id)
       friend = User.objects.get(id=id)
    except:
        messages.info(request, 'show Not Found')
        return redirect('/home')
    context = {
        "user":user,
        "friend":friend,
    }
    return render(request, 'app/detail_others.html', context)

def show(request, id):
    try:
       user = User.objects.get(id=id)
       friend = User.objects.get(id=id)
    except:
        messages.info(request, 'show Not Found')
        return redirect('/home')
    context = {
        "user":user,
        "friend":friend,
    }
    return render(request, 'app/detail.html', context)
def add_friend(request,id):
    user = User.objects.get(id=request.session['userId'])
    friend = User.objects.get(id=id)
    user.friends.add(friend)
    return redirect('/home')

def remove_friend(request,id):
    user = User.objects.get(id=request.session['userId'])
    friend = User.objects.get(id=id)
    user.friends.remove(friend)
    return redirect('/home')

