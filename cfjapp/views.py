from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegisterForm
from .models import ProduceModel,NewUser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re

# Create your views here.

def index(req):

    homeShowList = ProduceModel.objects.order_by('sortid')
    homeShowList = ProduceModel.objects.order_by('sortid')
    loginForms = LoginForm()
    reqCtx = RequestContext(req,{})
    return render(req,'index.html',{'homeShowList':homeShowList,'loginForms':loginForms})
def aboutus(req):
    return render(req,'about.html',{})
def ourStory(req):
    return render(req,'our_story.html',{})
def menu(req):
    return render(req,'menu.html',{})
def order(req):
    return render(req,'shopping_cart_step_1.html',{})
def shop_step_one(req):
    return render(req,'shopping_cart_step_1.html',{})
def shop_step_two(req):
    return render(req,'shopping_cart_step_2.html',{})
def shop_step_three(req):
    return render(req,'shopping_cart_step_3.html',{})
def shop(req):
    return render(req,'shop.html',{})
def location(req):
    return render(req,'locations.html',{})
def contact(req):
    return render(req,'contact.html',{})
def cf_login(req):
    if req.method == 'GET':
        form = LoginForm()
        return render(req, 'login.html', {'form': form})
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                print('login Success')
                url = req.POST.get('', '/index')
                return redirect(url)
            else:
                print("出错了")
                return render(req, 'login.html', {'form': form, 'error': "用户名或者密码错误"})
        else:

            return render(req, 'login.html', {'form': form})
    return render(req,'login.html',{})
def cf_logout(req):
    url = req.POST.get('','/index')
    logout(req)
    return redirect(url)

def cf_register(req):
    error_msg = None
    if req.method == 'GET':
        form = RegisterForm()
        return render(req,'register.html',{'form':form})
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            return render(req, 'register.html', {'form': form})
        else:
            pass
    return render(req,'register.html',{"error_msg":"error","form":form})

def register_yanzheng(req):
    type = req.GET.get('type')
    yz_text = req.GET.get("text")
    form = RegisterForm()
    if type == 'phone':
        # 验证手机号
        try:
            user = NewUser.objects.get(phonenum=yz_text)
        except ObjectDoesNotExist:
            data = {"flag": 1, "msg": "可以使用"}
            return JsonResponse({"callback": data})
        else:
            data = {"flag": 0, "msg": "该手机号码已被注册"}
            return JsonResponse({"callback": data})
    elif type == 'uname':
        try:
            user = NewUser.objects.get(username=yz_text)
        except ObjectDoesNotExist:
            data = {"flag": 1, 'msg': "可以使用"}
            return JsonResponse({"callback": data})
        else:
            data = {"flag": 0, "msg": "该账号已被注册"}
            return JsonResponse({"callback": data})
    else:
        print('???')
        # return render(req, 'register.html', {"error_msg": "error", "form": form})

@csrf_exempt
def register_submit(req):
    username = req.POST['username']
    pwd = req.POST['pwd']
    emial = req.POST['email']
    phone = req.POST['phone']
    c_user = NewUser()
    c_user.username = username
    c_user.phonenum = phone
    c_user.email = emial
    c_user.password = pwd
    c_user.save()
    bData = {"flag": 1, "msg": "success"}
    return JsonResponse({"callback":bData})


def yanzhengWithType(type,text,repwd):
    if type == 'uname':
        if len(text) <5 or len(text) > 12:
            return (False,'请输入5-12位用户名')
        user = NewUser.objects.get(username=text)
        if(user):
            return (False,'该用户已经存在')

    if type == 'email':
        regexStr = r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
        result = re.match(regexStr,text)
        if result == False:
            return (False,"邮箱地址不正确")

    if type == 'pwd':
        if len(text) <6 or len(text) > 18:
            return (False,'请输入6-18位密码')
        elif (text != repwd):
            return (False,"两次密码不同")

    if type == "phone":
        regexStr = r"1\d{10}"
        result = re.match(regexStr, text)
        if result == False:
            return (False, "手机号码格式不正确")

        user = NewUser.objects.get(phonenum=text)
        if(user):
            return (False,"该手机号码已存在")

    return (True,"Success")