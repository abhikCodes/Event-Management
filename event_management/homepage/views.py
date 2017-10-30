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
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, LoginForm, clubForm, ForgotPassForm
import json
from .models import Reg_User,Clubs,eve_detail



# Create your views here.
def home(request):
    form = UserRegistrationForm()
    form1 = LoginForm()
    return render(request, 'homepage/index.html', {'form': form, 'form1': form1})

def club(request):
    return render(
        request, 'homepage/clubs.html',{}
        )    

def ForgotPass(request):
    print("Halo ! Bhool Gya Password...")
    if request.method == 'POST':
        form = ForgotPassForm(request.POST)
        if form.is_valid():
                subject = "Welcome to SNU club Management"
                message = "Welcome to the Event Management System for SNU. Let's put an end to the frustating spam emails. Welcome to an all new experience of getting notified about the howabouts at SNU."
                from_email = settings.EMAIL_HOST_USER
                to_list = [email, settings.EMAIL_HOST_USER]
                send_mail(subject,message,from_email,to_list )
    else:
        form = ForgotPassForm()
        return render(
            request, 'homepage/index.html',{"form": form}
        )

def register(request):
    print("Halo ! Let's Play...")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            name = userObj['name']
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            confirm = userObj['confirmpass']
            print("Username and password and confirmpassword is as follows:- ", username,password,confirm)
            if(password==confirm):
                subject = "Welcome to SNU club Management"
                message = "Welcome to the Event Management System for SNU. Let's put an end to the frustating spam emails. Welcome to an all new experience of getting notified about the howabouts at SNU."
                from_email = settings.EMAIL_HOST_USER
                to_list = [email, settings.EMAIL_HOST_USER]
                send_mail(subject,message,from_email,to_list )
                x=Reg_User.objects.all()
                print(len(x))
                # print(x['email'])
                # print("X==",x," type= ",type(x))
                # for i in x:
                #     print(i.id)
                #     print(i.Username)

                print(username, email)
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    Reg_User_instance = Reg_User.objects.create(id=len(x) + 1, Name=name, Username=username,
                                                                Email=email, Password=password, interests="")
                    User.objects.create_user(username, email, password)
                    user = authenticate(username = username, password = password)
                    # login(request, user)
                    return HttpResponseRedirect('/tag')
                else:
                    raise forms.ValidationError('Looks like a username with that email or password already exists')
            else:
                raise forms.ValidationError('Password not confirmed.')
    else:
        form = UserRegistrationForm()
        form1 = LoginForm()
    return render(request, 'homepage/tag.html', {'form' : form, 'form1':form1})

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
        print("XYZ")
        print(form)
        print(form.is_valid())
        # print(form.cleaned_data['email'])
        # print(form.cleaned_data['password'])
        # user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        # print("user===", user)
        # login(request, user)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            # email = userObj['email']
            password =  userObj['password']
            # print(email,password)
            user = authenticate(username=username , password = password)
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
    myElem=Reg_User.objects.all()
    myElem=myElem[len(myElem)-1]
    reqId=myElem.id
    print("reqId=",reqId)
    interest = request.POST
    x=interest.getlist('recommendations')
    print("x== ",x)
    entry=Reg_User.objects.get(id=reqId)
    print("entry.id= ",entry.id)
    tags=",".join(x)
    print(tags)
    entry.interests=tags
    print(entry.interests)
    entry.save()

    # y = Reg_User.objects.all()
    # print(len(y))
    # if request.method == 'POST':

    return HttpResponseRedirect("/")

    # return render(
    #     request, 'homepage/index.html', {'interest':x}
    # )
    # else:
    #     return "<h1>Fo</h1>"


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

def events_detail(request, pk):
    post = get_object_or_404(eve_detail, pk=pk)
    return render(
        request, 'homepage/events.html', {'post': post}
        )