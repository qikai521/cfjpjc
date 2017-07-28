from django import forms
from .models import User
from django.core.exceptions import ValidationError

import re



class LoginForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'class':'login_form-control','id':'uid','placeholder':'账号/手机号'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login_form-control','id':'pwd','placeholder':'密码'}))

class RegisterForm(forms.Form):
    uname = forms.CharField(widget=forms.TextInput(attrs={"class":"input_uanme useblur","id":"inputid_uname","placeholder":"请输入登录账号*","data-min":"5","data-max":"10","onblur":"checkWithType('uname')"},))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input_pwd useblur","id":"inputid_pwd","placeholder":"请输入密码*","data-match":"inputid_repwd","data-min":"5","data-max":"10","onblur":"checkWithType('pwd')"}))
    repwd = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input_repwd useblur","id":"inputid_repwd","placeholder":"重新输入密码*","data-match":"inputid_repwd","data-min":"5","data-max":"10","onblur":"checkWithType('repwd')"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"input_email useblur","id":"inputid_email","placeholder":"请输入邮箱","data-type":"email","onblur":"checkWithType('email')"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"input_phone useblur","id":"inputid_phone","placeholder":"请输入手机号码*","onblur":"checkWithType('phone')"}))
    code = forms.CharField(widget=forms.TextInput(attrs={"class":"input_code useblur","id":"inputid_code","placeholder":"输入验证码*","onblur":"checkWithType('code')"}))










