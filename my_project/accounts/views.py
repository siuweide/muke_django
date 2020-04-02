from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from accounts.form import UserLoginForm, UserRegisterForm, UserAddressForm
# from django.contrib.auth.models import User
from accounts.models import User, UserAddress
from utils import constants
from utils.verify import VerifyCode


def user_login(request):
    next_url = request.GET.get('next', 'index')
    if request.method == 'POST':
        form = UserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # # 查询用户的信息
            # user = User.objects.get(username=username, password=password)
            # # 设置用户ID到session
            # request.session[constants.LOGIN_SESSION_ID] = user.id
            # # 登录后跳转到首页
            # return redirect('index')

            # 使用django自带的authenticate用户进行登录
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(next_url)
        else:
            print(form.errors)
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html' ,{
        'form':form,
        'next_url':next_url
    })

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request=request, data=request.POST)
        if form.is_valid():
            # 创建用户
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nickname = form.cleaned_data['nickname']
            User.objects.create_user(username=username,
                                     password=password,
                                     level=0,
                                     nickname=nickname)
            # 登录
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('index')

    else:
        form = UserRegisterForm(request=request)
    return render(request, 'register.html', {
        'form':form
    })


def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def address_list(request):
    """ 列表地址 """
    address_list = UserAddress.objects.filter(user=request.user, is_valid=True).order_by('-is_default')
    return render(request, 'address_list.html', {
        'address_list':address_list
    })

@login_required
def address_add(request):
    """ 列表添加 """
    if request.method == 'POST':
        form = UserAddressForm(request=request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:address_list')
    else:
        form = UserAddressForm(request=request)
    return render(request, 'address_add.html', {
        'form':form
    })

@login_required
def address_edit(request, pk):
    """ 编辑收货地址 """
    user = request.user
    initial = {}
    if str(pk).isdigit():
        addr = get_object_or_404(UserAddress, id=pk, user=user, is_valid=True)
        initial['region'] = addr.get_region_format
    if request.method == 'POST':
        form = UserAddressForm(request=request,data=request.POST, instance=addr, initial=initial)
        if form.is_valid():
            form.save()
            return redirect('accounts:address_list')
    else:
        form = UserAddressForm(request=request, instance=addr, initial=initial)
    return render(request, 'address_edit.html', {
        'form':form,
        'pk':pk
    })

def address_delete(request, pk):
    addr = get_object_or_404(UserAddress, pk=pk, is_valid=True, user=request.user)
    addr.is_valid = False
    addr.save()
    return HttpResponse('ok')
