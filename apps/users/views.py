from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from users.models import Users

from utils.response import HandleResponse


# Create your views here.


class Test(View):
    def get(self, request):
        return JsonResponse({'code': '0', 'date': 'successs'})


class Login(View):
    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据
        if not all([username, password]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)

        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登录状态
                login(request, user)

                # 返回response
                data = Users.objects.get(username=username)
                return_data = {
                    "username": data.username,
                    "email": data.email,
                    "avatar": str(data.avatar),
                    "area": data.area
                }
                return HandleResponse(return_data, '登录成功').response_json()
            else:
                # 用户未激活
                return HandleResponse({}, '账户未激活', 30002).response_json()
        else:
            # 用户名或密码错误
            return HandleResponse({}, '用户名或密码错误', 30003).response_json()


class Logout(View):
    def post(self, request):
        logout(request)
        return HandleResponse({}, '登出成功').response_json()
