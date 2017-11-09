"""from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
"""
from django import forms
from django.contrib.auth import authenticate, login

class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'Name',
        max_length = 32
    )
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 320,
        widget = forms.PasswordInput()
    )
    confirmpass = forms.CharField(
        required=True,
        label='Confirm Password',
        max_length=320,
        widget=forms.PasswordInput()
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    # email = forms.EmailField(
    #     required=True,
    #     label='Email',
    #     max_length=32,
    # )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=320,
        widget=forms.PasswordInput()
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # user = authenticate(email=email , password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        print("Cleaned data Object is : -",self.cleaned_data)
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # user = authenticate(email=email , password=password)
        return user


class clubForm(forms.Form):
    clubname = forms.CharField(
        required = True,
        label = 'clubname',
        max_length = 32
    )

class ForgotPassForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=32,
    )

class ChangePassForm(forms.Form):

    password = forms.CharField(
        required=True,
        label='New Password',
        max_length=32,
        widget=forms.PasswordInput(),
        # blank=False,
        # null=False,
    )

    confirm = forms.CharField(
        required=True,
        label='Confirm New Password',
        max_length=32,
        widget=forms.PasswordInput(),
        # blank=False,
        # null=False,
    )

class EmailCustomizeForm(forms.Form):
    Subject = forms.CharField(
        required=True,
        label='Subject',
        max_length=320,
        # widget=forms.PasswordInput(),
        # blank=False,
        # null=False,
    )

    body = forms.CharField(
        required=True,
        label='Message Body',
        max_length=3200,
        # widget=forms.PasswordInput(),
        # blank=False,
        # null=False,
    )