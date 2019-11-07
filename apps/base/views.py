from django.views.generic import View
from base.models import Banner, AreaInfo
from django.utils.decorators import method_decorator
from django.conf import settings

from utils.response import HttpResponseJson
from utils.my_decorator import MyDecorator

from django.core import serializers
import json


# 递归返回城市
def recursion(allArea, data):
    """
    :param allArea: 所有城市列表
    :param data: 返回的数据
    :return:
    """
    for item in data:
        item['children'] = []
        for list in allArea:
            if list['fields']['aParent'] == item['pk']:
                item['children'].append(list)
        if len(item['children']) != 0:
            recursion(allArea, item['children'])

    return data


class AreaView(View):
    @method_decorator(MyDecorator.is_login)  # 通过给dispatch方法添加装饰器判断是否登录
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """查询区域api"""
        atitle = ''
        data = json.loads(serializers.serialize("json", AreaInfo.objects.filter(atitle__contains=atitle)))
        allArea = []
        topArea = []
        for item in data:
            allArea.append(item)
            if item['fields']['aParent'] == None:
                topArea.append(item)
        if request.GET.get('atitle'):
            atitle = request.GET.get('atitle')
            dataLists = json.loads(serializers.serialize("json", AreaInfo.objects.filter(atitle__contains=atitle)))
            return HttpResponseJson(data=recursion(allArea, dataLists)).json()
        else:
            return HttpResponseJson(data=recursion(allArea, topArea)).json()


class BannerView(View):
    @method_decorator(MyDecorator.is_login)  # 通过给dispatch方法添加装饰器判断是否登录
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """查询banner"""
        data = Banner.objects.filter(is_delete=False)
        for item in data:
            item.image = 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL + str(item.image)
        return HttpResponseJson(data=data).json()

    def post(self, request):
        id = request.POST.get('id', None)
        index = request.POST.get('index')
        url = request.POST.get('url')
        image = request.FILES.get('image', None)

        if id:  # 修改
            try:
                data = Banner.objects.get(id=id)
            except:
                return HttpResponseJson(status=500, code=50001).json()
            if index:
                data.index = index
            if url:
                data.url = url
            if image:
                data.image = image
            data.save()
            return HttpResponseJson(data='修改成功').json()
        else:  # 添加
            if not all([index, url, image]):
                return HttpResponseJson(status=400, code=40000).json()
            Banner.objects.create(
                index=index,
                url=url,
                image=image
            )
            return HttpResponseJson(data='添加成功').json()

    def delete(self, request):
        id = request.GET.get('id')
        if not all([id]):
            return HttpResponseJson(status=400, code=40000).json()
        Banner.objects.filter(id=id).update(is_delete=True)
        return HttpResponseJson(data='删除成功').json()
