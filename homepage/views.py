from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, LoginForm
import json

# Create your views here.
def home(request):
    return render(
    	request, 'homepage/index.html', {}
    	)
def club(request):
	return render(
		request, 'homepage/clubs.html',{}
		)    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                # login(request, user)
                return HttpResponseRedirect('/login')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
        form1 = LoginForm()
    return render(request, 'homepage/LoginPage.html', {'form' : form, 'form1':form1})			

def Login(request):
    # form = LoginForm(request.POST or None)
    # if request.POST and form.is_valid():
    #     user = form.login(request)
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect("/n1.html")# Redirect to a success page.
    # form = UserRegistrationForm()
    # form1 = LoginForm()
    # print(type(form))
    # return render(request, 'homepage/LoginPage.html', {'form' : form, 'form1':form1})
    # return render(request, 'enter.html', {'login_form': form })
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password']
            print("Username and password is as follows:- ", username,password)
            user = authenticate(username = username, password = password)
            print("user===",user)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            raise forms.ValidationError('Wrong Credentials entered')
    else:
        form = UserRegistrationForm()
        form1 = LoginForm()
        # form = LoginForm()
        print(form)
        return render(request, 'homepage/LoginPage.html', {'form' : form, 'form1':form1})