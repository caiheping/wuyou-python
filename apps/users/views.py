from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

from users.models import Users

from utils.response import HttpResponseJson


# Create your views here.


class Login(View):
    """登录"""
    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据
        if not all([username, password]):
            return HttpResponseJson(status=400, code=40000).json()

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)

        if user is not None:
            # 用户已激活
            # 记录用户的登录状态
            login(request, user)

            # 返回response
            data = Users.objects.get(username=username)
            if data.avatar:
                avatar = 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL + str(data.avatar)
            else:
                avatar = str(data.avatar)
            return_data = {
                "username": data.username,
                "email": data.email,
                "avatar": avatar,
                "area": data.area
            }
            return HttpResponseJson(data=return_data).json()
        else:
            # 用户名或密码错误
            return HttpResponseJson(status=400, code=40002).json()


class Logout(View):
    """登出"""
    def post(self, request):
        logout(request)
        return HttpResponseJson(data='退出成功').json()
