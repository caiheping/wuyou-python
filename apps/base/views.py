from django.views.generic import View
from base.models import Banner, AreaInfo
from utils.response import HandleResponse


# Create your views here.


class GetArea(View):
    def get(self, request):
        """查询区域api"""
        atitle = ''
        if request.GET.get('atitle'):
            atitle = request.GET.get('atitle')

        data = AreaInfo.objects.filter(atitle__contains=atitle)
        return HandleResponse(data).response_json()


class GetBanner(View):
    def get(self, request):
        """查询banner"""
        data = Banner.objects.all()
        arr = []
        for item in data:
            arr.append({
                'image': item.image,
                'url': item.url
            })
        return HandleResponse(arr).response_json()


class Test(View):
    def get(self, request):
        data = ({'a': 'fff'},)
        return HandleResponse(data).response_json()
