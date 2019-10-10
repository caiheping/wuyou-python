from django.views.generic import View
from base.models import Banner, AreaInfo
from django.utils.decorators import method_decorator

from utils.response import HandleResponse
from utils.my_decorator import MyDecorator


class AreaView(View):
    @method_decorator(MyDecorator.is_login)  # 通过给dispatch方法添加装饰器判断是否登录
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """查询区域api"""
        atitle = ''
        if request.GET.get('atitle'):
            atitle = request.GET.get('atitle')
        data = AreaInfo.objects.filter(atitle__contains=atitle)
        return HandleResponse(data).response_json()


class BannerView(View):
    @method_decorator(MyDecorator.is_login)  # 通过给dispatch方法添加装饰器判断是否登录
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """查询banner"""
        data = Banner.objects.filter(is_delete=False)
        arr = []
        for item in data:
            arr.append({
                'image': str(item.image),
                'url': item.url
            })
        return HandleResponse(arr).response_json()

    def post(self, request):
        id = request.POST.get('id', None)
        index = request.POST.get('index')
        url = request.POST.get('url')
        image = request.FILES.get('image', None)

        if id:  # 修改
            Banner.objects.filter(id=id).update(
                index=index,
                url=url,
                image=image
            )
            return HandleResponse({}, '修改成功').response_json()
        else:   # 添加
            if not all([index, url, image]):
                return HandleResponse({}, '参数错误', 20000).response_json()
            Banner.objects.create(
                index=index,
                url=url,
                image=image
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        Banner.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()
