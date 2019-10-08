from django.views.generic import View
from django.http import JsonResponse
from django.core.paginator import Paginator

from companys.models import Companys
from utils.response import HandleResponse

# Create your views here.


class CompanysView(View):
    def get(self, request):
        id = request.GET.get('id')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 1)
        if not all([page, limit]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            data = Companys.objects.filter(id=id)
            return HandleResponse(data).response_json()
        else:
            data = Companys.objects.all().order_by('create_time')
            paginator = Paginator(data, limit)
            try:
                data_lists = paginator.page(page)
            except Exception as e:
                return HandleResponse({}, '没有此页码', 30001).response_json()
            return HandleResponse(data_lists.object_list).response_json()
