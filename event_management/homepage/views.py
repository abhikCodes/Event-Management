"""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from .models import Reg_User

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
            Reg_User_instance = Reg_User.objects.create(Username=username,Email=email,Password=password)
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'homepage/reg_form.html', {'form' : form})			
   
def tag(request):
    return render(
        request, 'homepage/tag.html', {}
        )
"""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, LoginForm, clubForm
import json
from .models import Reg_User,Clubs



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
            x=Reg_User.objects.all()
            print(len(x))
            # print(x['email'])
            # print("X==",x," type= ",type(x))
            # for i in x:
            #     print(i.id)
            #     print(i.Username)
            Reg_User_instance = Reg_User.objects.create(id=(len(x)+1),Username=username,Email=email,Password=password)
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                # login(request, user)
                return HttpResponseRedirect('/tag')
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
def tag(request):

    return render(
        request, 'homepage/tag.html', {}
        )
def sel_tag(request):
    interest = request.POST
    x=interest.getlist('recommendations')
    print("x== ",x)
    y = Reg_User.objects.all()
    print(len(y))
    if request.method == 'POST':

        return render(
            request, 'homepage/sel_tag.html', {'interest':x}
        )
    else:
        return "<h1>Fo</h1>"


def club(request,clubname):
    print("clubname= ",clubname)
    # x = Clubs.objects.all()
    x = Clubs.objects.filter(clubname=clubname.strip())
    print("length of queryset= ",len(x))
    print(x[0].clubname)

    # for i in x:
    #     print("Club=",i)
    # Reg_User_instance = Reg_User.objects.create(id=(len(x) + 1), Username=username, Email=email, Password=password)
    # if request.method == 'POST':
    #     interest = request.POST
    #     x = interest.getlist('recommendations')
    #     print("x== ", x)
    #     form = clubForm(request.POST)
    #     if form.is_valid():
    #         userObj = form.cleaned_data
    #         print(userObj['club'])

    # clubName=request.club
    # print(clubName)
    # else:
    return  render(
        request, 'homepage/club.html', {"clubname":clubname }
    )