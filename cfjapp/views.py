from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegisterForm
from .models import ProduceModel,NewUser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def index(req):
    print('index')
    print(req)
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
            print(form.errors)
            print("not valid")
            return render(req, 'login.html', {'form': form})
    return render(req,'login.html',{})
def cf_logout(req):
    url = req.POST.get('','/index')
    logout(req)
    print('logout')
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
            print("success")
            return render(req, 'register.html', {'form': form})
        else:
            print(form.errors)

    return render(req,'register.html',{"error_msg":"error","form":form})

def cf_test(req):
    return JsonResponse({"name":"qikai","age":18})
@csrf_exempt
def register_yanzheng(req):
    type = req.GET.get('type')
    yz_text = req.GET.get("text")
    print(type, yz_text)
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



