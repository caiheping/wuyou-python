from django.views.generic import View
from django.core.paginator import Paginator
from django.conf import settings

from companys.models import Companys, Job, Welfare
from base.models import AreaInfo
from utils.response import HttpResponseJson

# Create your views here.


class CompanysView(View):
    """公司API"""
    def get(self, request):
        id = request.GET.get('id')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 1)
        if id:
            try:
                data = Companys.objects.filter(id=id, is_delete=False).values()[0]
                return HttpResponseJson(data).json()
            except Exception as e:
                return HttpResponseJson(status=500, code=50001).json()
        else:
            if not all([page, limit]):
                return HttpResponseJson(status=400, code=40000).json()
            data = Companys.objects.filter(is_delete=False).order_by('-create_time')
            paginator = Paginator(data, limit)
            try:
                data_lists = paginator.page(page)
            except Exception as e:
                return HttpResponseJson(status=400, code=40001).json()
            for item in data_lists.object_list:
                item.logoImg = 'http://'+request.META['HTTP_HOST']+settings.STATIC_URL+str(item.logoImg)
            return HttpResponseJson(data=data_lists.object_list).json()

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        logoImg = request.FILES.get('logoImg')
        type = request.POST.get('type')
        addr = request.POST.get('addr')
        area = request.POST.get('area')
        introduce = request.POST.get('introduce')
        personnel = request.POST.get('personnel')
        company_start_time = request.POST.get('company_start_time')

        if id:
            try:
                data = Companys.objects.get(id=id)
            except:
                return HttpResponseJson(status=500, code=50001).json()
            if name:
                data.name = name
            if logoImg:
                data.logoImg = logoImg
            if type:
                data.type = type
            if addr:
                data.addr = addr
            if area:
                data.area = AreaInfo.objects.get(id=area)
            if introduce:
                data.introduce = introduce
            if personnel:
                data.personnel = personnel
            if company_start_time:
                data.company_start_time = company_start_time
            data.save()
            return HttpResponseJson(data='修改成功').json()
        else:
            if not all([name, logoImg, type, addr, area, introduce, personnel, company_start_time]):
                return HttpResponseJson(status=400, code=40000).json()
            Companys.objects.create(
                name=name,
                logoImg=logoImg,
                type=type,
                addr=addr,
                area=AreaInfo.objects.get(id=area),
                introduce=introduce,
                personnel=personnel,
                company_start_time=company_start_time
            )
            return HttpResponseJson(data='添加成功').json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HttpResponseJson(status=400, code=40000).json()
        Companys.objects.filter(id=id).update(is_delete=True)
        return HttpResponseJson(data='删除成功').json()


class JobView(View):
    """职业API"""
    def get(self, request):
        id = request.GET.get('id')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 1)
        if id:
            try:
                data = Job.objects.filter(id=id, is_delete=False).values()[0]
                return HttpResponseJson(data).json()
            except:
                return HttpResponseJson(status=500, code=50001).json()
        else:
            if not all([page, limit]):
                return HttpResponseJson(status=400, code=40000).json()
            data = Job.objects.filter(is_delete=False).order_by('-create_time')
            paginator = Paginator(data, limit)
            try:
                data_lists = paginator.page(page)
            except Exception as e:
                return HttpResponseJson(status=400, code=40001).json()
            return HttpResponseJson(data=data_lists.object_list).json()

    def post(self, request):
        id = request.POST.get('id')
        job = request.POST.get('job')
        company = request.POST.get('company')
        min_salary = request.POST.get('min_salary')
        max_salary = request.POST.get('max_salary')
        describe = request.POST.get('describe')
        working_years = request.POST.get('working_years')
        education = request.POST.get('education')
        recruitment = request.POST.get('recruitment')

        if id:
            try:
                data = Job.objects.get(id=id)
            except:
                return HttpResponseJson(status=500, code=50001).json()
            if job:
                data.job = job
            if company:
                data.company = Companys.objects.get(id=company)
            if min_salary:
                data.min_salary = min_salary
            if max_salary:
                data.max_salary = max_salary
            if describe:
                data.describe = describe
            if working_years:
                data.working_years = working_years
            if education:
                data.education = education
            if recruitment:
                data.recruitment = recruitment
            data.save()
            return HttpResponseJson(data='修改成功').json()
        else:
            if not all([job, company, min_salary, max_salary, describe, working_years, education, recruitment]):
                return HttpResponseJson(status=400, code=40000).json()
            Job.objects.create(
                job=job,
                company=Companys.objects.get(id=company),
                min_salary=min_salary,
                max_salary=max_salary,
                describe=describe,
                working_years=working_years,
                education=education,
                recruitment=recruitment
            )
            return HttpResponseJson(data='添加成功').json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HttpResponseJson(status=400, code=40000).json()
        Job.objects.filter(id=id).update(is_delete=True)
        return HttpResponseJson(data='删除成功').json()


class WelfareView(View):
    """公司福利API"""
    def get(self, request):
        company = request.GET.get('company')
        if not all([company]):
            return HttpResponseJson(status=400, code=40000).json()
        try:
            data = Welfare.objects.filter(is_delete=False, company=Companys.objects.get(id=company))
            return HttpResponseJson(data).json()
        except:
            return HttpResponseJson(status=500, code=50000).json()

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        company = request.POST.get('company')

        if id:
            try:
                data = Welfare.objects.get(id=id)
            except:
                return HttpResponseJson(status=500, code=50001).json()
            if name:
                data.name = name
            if company:
                data.company = Companys.objects.get(id=company)
            data.save()
            return HttpResponseJson(data='修改成功').json()
        else:
            if not all([name, company]):
                return HttpResponseJson(status=400, code=40000).json()
            try:
                Welfare.objects.create(
                    name=name,
                    company=Companys.objects.get(id=company)
                )
                return HttpResponseJson(data='添加成功').json()
            except:
                return HttpResponseJson(status=500, code=50000).json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HttpResponseJson(status=400, code=40000).json()
        Welfare.objects.filter(id=id).update(is_delete=True)
        return HttpResponseJson(data='删除成功').json()
