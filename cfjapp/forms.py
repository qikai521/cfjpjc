from django import forms
from .models import User
from django.core.exceptions import ValidationError

import re



class LoginForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'class':'login_form-control','id':'uid','placeholder':'账号/手机号'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login_form-control','id':'pwd','placeholder':'密码'}))

class RegisterForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "请输入邮箱账号", "value": "", "required": "required", }),
                                max_length=50, error_messages={"required": "用户名不能为空", })
    phonenum = forms.CharField(widget=forms.TextInput(attrs={'class':'login_form-control','id':'phonenum333','placeholder':'手机号码','onblur':"__changeUserName('phonenum')"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"register_input","id":"email","name":"email","maxLength":"50","value":"","onblur":"__changeUserName('email')"}))


class TestForm(forms.Form):
    username = forms.RegexField(
        required=True,
        max_length=30,
        regex='^ppp',
        error_messages={
                'required': 'ERROR_USERNAME_REQUIRED',
                'max_length': 'ERRROR_FIELD_TOO_LONG',
                'invalid': 'ERROT_INVALID_USERNAME',
        },
       label='username')

    password1 = forms.CharField(
        required=True,
        max_length=30,
        error_messages={
            'required': 'ERROR_PASSWD_REQUIRED',
            'max_length': 'ERRROR_FIELD_TOO_LONG',
        },
        label='password1',  widget=forms.PasswordInput)

    password2 = forms.CharField(
        required=True,
        max_length=30,
        error_messages={
            'required': 'ERROR_PASSWD_REQUIRED',
            'max_length': 'ERRROR_FIELD_TOO_LONG',
        },
        label='password2',  widget=forms.PasswordInput)

    email = forms.EmailField(required=False)


    def clean_username(self):
        username = self.cleaned_data['username']
        exist = User.objects.filter(username=username).count()
        if exist:
            raise forms.ValidationError('ERROR_ACCOUNT_EXISTED')
        else:
            self.cleaned_data['username'] = username
        return self.cleaned_data['username']

    def clean_password1(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise forms.ValidationError('ERROR_PASSWD_NOT_SAME')
        return self.cleaned_data['password1']

