from django.views.generic import View
from django.core.paginator import Paginator

from companys.models import Companys, Job, Welfare
from base.models import AreaInfo
from utils.response import HandleResponse

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
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            if not all([page, limit]):
                return HandleResponse({}, '参数错误', 20000).response_json()
            data = Companys.objects.filter(is_delete=False).order_by('-create_time')
            paginator = Paginator(data, limit)
            try:
                data_lists = paginator.page(page)
            except Exception as e:
                return HandleResponse({}, '没有此页码', 30001).response_json()
            return HandleResponse(data_lists.object_list).response_json()

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        logoImg = request.POST.get('logoImg')
        type = int(request.POST.get('type'))
        addr = request.POST.get('addr')
        area = int(request.POST.get('area'))
        introduce = request.POST.get('introduce')
        personnel = request.POST.get('personnel')
        company_start_time = request.POST.get('company_start_time')

        if not all([name, logoImg, type, addr, area, introduce, personnel, company_start_time]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            Companys.objects.filter(id=id).update(
                name=name,
                logoImg=logoImg,
                type=type,
                addr=addr,
                area=area,
                introduce=introduce,
                personnel=personnel,
                company_start_time=company_start_time
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
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
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        Companys.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class JobView(View):
    """职业API"""
    def get(self, request):
        id = request.GET.get('id')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 1)
        if id:
            try:
                data = Job.objects.filter(id=id, is_delete=False).values()[0]
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            if not all([page, limit]):
                return HandleResponse({}, '参数错误', 20000).response_json()
            data = Job.objects.filter(is_delete=False).order_by('-create_time')
            paginator = Paginator(data, limit)
            try:
                data_lists = paginator.page(page)
            except Exception as e:
                return HandleResponse({}, '没有此页码', 30001).response_json()
            return HandleResponse(data_lists.object_list).response_json()

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

        if not all([job, company, min_salary, max_salary, describe, working_years, education, recruitment]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            Job.objects.filter(id=id).update(
                job=job,
                company=company,
                min_salary=min_salary,
                max_salary=max_salary,
                describe=describe,
                working_years=working_years,
                education=education,
                recruitment=recruitment
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
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
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        Job.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class WelfareView(View):
    """公司福利API"""
    def get(self, request):
        company = request.GET.get('company')
        if not all([company]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        try:
            data = Welfare.objects.filter(is_delete=False, company=Companys.objects.get(id=company))
            return HandleResponse(data).response_json()
        except:
            return HandleResponse({}, '服务器错误', 40000).response_json()

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        company = request.POST.get('company')

        if not all([name, company]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            Welfare.objects.filter(id=id).update(
                name=name,
                company=Companys.objects.get(id=company)
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            try:
                Welfare.objects.create(
                    name=name,
                    company=Companys.objects.get(id=company)
                )
                return HandleResponse({}, '添加成功').response_json()
            except:
                return HandleResponse({}, '服务器错误', 40000).response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        Welfare.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()
