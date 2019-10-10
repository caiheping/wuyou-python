from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
import json

from resumes.models import Resume, ResumeWorking, ResumeEducation, ResumeJob, ResumeProjectExperience
from users.models import Users
from utils.response import HandleResponse

# Create your views here.


class ShowResumeView(View):
    """显示简历全部信息"""
    def get(self, request):
        id = request.GET.get('id')
        resume = json.loads(serializers.serialize("json", Resume.objects.filter(id=id, is_delete=False)))
        resumeWorking = json.loads(serializers.serialize("json", ResumeWorking.objects.filter(resume__id=id, is_delete=False)))
        resumeEducation = json.loads(serializers.serialize("json", ResumeEducation.objects.filter(resume__id=id, is_delete=False)))
        resumeJob = json.loads(serializers.serialize("json", ResumeJob.objects.filter(resume__id=id, is_delete=False)))
        resumeProjectExperience = json.loads(serializers.serialize("json", ResumeProjectExperience.objects.filter(resume__id=id, is_delete=False)))

        obj = {
            "resume": resume,
            "resumeWorking": resumeWorking,
            "resumeEducation": resumeEducation,
            "resumeJob": resumeJob,
            "resumeProjectExperience": resumeProjectExperience,
        }
        return JsonResponse(obj, safe=False)


class ResumeView(View):
    """简历基本信息"""
    def get(self, request):
        id = request.GET.get('id')
        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        try:
            data = Resume.objects.filter(id=id, is_delete=False).values()[0]
            return HandleResponse(data).response_json()
        except Exception as e:
            return HandleResponse({}, '没有此记录', 30002).response_json()

    def post(self, request):
        u_id = request.POST.get('u_id')
        name = request.POST.get('name')
        is_open = request.POST.get('is_open', 0)
        progress = request.POST.get('progress', 0)
        username = request.POST.get('username')
        pic = request.FILES.get('pic', None)
        sex = request.POST.get('sex', 'female')
        birthday = request.POST.get('birthday', None)
        phone = request.POST.get('phone', None)
        status = request.POST.get('status', 0)
        start_working = request.POST.get('start_working', None)
        addr = request.POST.get('addr')
        email = request.POST.get('email', None)
        ID_number = request.POST.get('ID_number', None)
        annual_income = request.POST.get('annual_income', 0)
        hukou_or_nationality = request.POST.get('hukou_or_nationality', None)
        marital_status = request.POST.get('marital_status', 0)

        if not all([u_id, name, username, pic, addr]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        is_exist = Resume.objects.filter(user__id=u_id)

        if is_exist:
            Resume.objects.filter(user__id=u_id).update(
                name=name,
                is_open=is_open,
                progress=progress,
                username=username,
                pic=pic,
                sex=sex,
                birthday=birthday,
                phone=phone,
                status=status,
                start_working=start_working,
                addr=addr,
                email=email,
                ID_number=ID_number,
                annual_income=annual_income,
                hukou_or_nationality=hukou_or_nationality,
                marital_status=marital_status,
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            Resume.objects.create(
                user=Users.objects.get(id=u_id),
                name=name,
                is_open=is_open,
                progress=progress,
                username=username,
                pic=pic,
                sex=sex,
                birthday=birthday,
                phone=phone,
                status=status,
                start_working=start_working,
                addr=addr,
                email=email,
                ID_number=ID_number,
                annual_income=annual_income,
                hukou_or_nationality=hukou_or_nationality,
                marital_status=marital_status,
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        Resume.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class ResumeWorkingView(View):
    """工作经验"""
    def get(self, request):
        id = request.GET.get('id')
        resume_id = request.GET.get('resume_id')
        if not all([resume_id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            try:
                data = ResumeWorking.objects.filter(id=id, resume__id=resume_id, is_delete=False).values()[0]
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            data = ResumeWorking.objects.filter(resume__id=resume_id, is_delete=False)
            return HandleResponse(data).response_json()

    def post(self, request):
        id = request.POST.get('id')
        resume_id = request.POST.get('resume_id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        company = request.POST.get('company')
        position = request.POST.get('position')
        job_description = request.POST.get('job_description')
        industry = request.POST.get('industry', None)
        department = request.POST.get('department', None)
        nature = request.POST.get('nature', None)
        other = request.POST.get('other', None)
        type = request.POST.get('type', None)

        if not all([resume_id, start_time, end_time, company, position, job_description]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            ResumeWorking.objects.filter(id=id).update(
                resume=Resume.objects.get(id=resume_id),
                start_time=start_time,
                end_time=end_time,
                company=company,
                position=position,
                job_description=job_description,
                industry=industry,
                department=department,
                nature=nature,
                other=other,
                type=type,
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            ResumeWorking.objects.create(
                resume=Resume.objects.get(id=resume_id),
                start_time=start_time,
                end_time=end_time,
                company=company,
                position=position,
                job_description=job_description,
                industry=industry,
                department=department,
                nature=nature,
                other=other,
                type=type,
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        ResumeWorking.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class ResumeEducationView(View):
    """教育经历"""
    def get(self, request):
        id = request.GET.get('id')
        resume_id = request.GET.get('resume_id')
        if not all([resume_id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            try:
                data = ResumeEducation.objects.filter(id=id, resume__id=resume_id, is_delete=False).values()[0]
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            data = ResumeEducation.objects.filter(resume__id=resume_id, is_delete=False)
            return HandleResponse(data).response_json()

    def post(self, request):
        id = request.POST.get('id')
        resume_id = request.POST.get('resume_id')
        enrollment_time = request.POST.get('enrollment_time')
        graduation_time = request.POST.get('graduation_time')
        school = request.POST.get('school')
        education = request.POST.get('education', 1)
        major = request.POST.get('major')
        major_desc = request.POST.get('major_desc', None)
        is_overseas_study = request.POST.get('is_overseas_study', 0)

        if not all([resume_id, enrollment_time, graduation_time, school, major]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            ResumeEducation.objects.filter(id=id).update(
                resume=Resume.objects.get(id=resume_id),
                enrollment_time=enrollment_time,
                graduation_time=graduation_time,
                school=school,
                education=education,
                major=major,
                major_desc=major_desc,
                is_overseas_study=is_overseas_study,
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            ResumeEducation.objects.create(
                resume=Resume.objects.get(id=resume_id),
                enrollment_time=enrollment_time,
                graduation_time=graduation_time,
                school=school,
                education=education,
                major=major,
                major_desc=major_desc,
                is_overseas_study=is_overseas_study,
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        ResumeEducation.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class ResumeJobView(View):
    """求职意向"""
    def get(self, request):
        id = request.GET.get('id')
        resume_id = request.GET.get('resume_id')
        if not all([resume_id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            try:
                data = ResumeJob.objects.filter(id=id, resume__id=resume_id, is_delete=False).values()[0]
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            data = ResumeJob.objects.filter(resume__id=resume_id, is_delete=False)
            return HandleResponse(data).response_json()

    def post(self, request):
        id = request.POST.get('id')
        resume_id = request.POST.get('resume_id')
        place = request.POST.get('place')
        function = request.POST.get('function')
        pay_type = request.POST.get('pay_type', 1)
        salary_expectation = request.POST.get('salary_expectation')
        work_type = request.POST.get('work_type', None)
        industry = request.POST.get('industry', None)
        arrival_time = request.POST.get('arrival_time', 1)
        self_evaluation = request.POST.get('self_evaluation')
        personal_tags = request.POST.get('personal_tags', None)

        if not all([resume_id, place, function, salary_expectation, self_evaluation]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            ResumeJob.objects.filter(id=id).update(
                resume=Resume.objects.get(id=resume_id),
                place=place,
                function=function,
                pay_type=pay_type,
                salary_expectation=salary_expectation,
                work_type=work_type,
                industry=industry,
                arrival_time=arrival_time,
                self_evaluation=self_evaluation,
                personal_tags=personal_tags,
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            ResumeJob.objects.create(
                resume=Resume.objects.get(id=resume_id),
                place=place,
                function=function,
                pay_type=pay_type,
                salary_expectation=salary_expectation,
                work_type=work_type,
                industry=industry,
                arrival_time=arrival_time,
                self_evaluation=self_evaluation,
                personal_tags=personal_tags,
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        ResumeJob.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()


class ResumeProjectExperienceView(View):
    """项目经验"""
    def get(self, request):
        id = request.GET.get('id')
        resume_id = request.GET.get('resume_id')
        if not all([resume_id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        if id:
            try:
                data = ResumeProjectExperience.objects.filter(id=id, resume__id=resume_id, is_delete=False).values()[0]
                return HandleResponse(data).response_json()
            except Exception as e:
                return HandleResponse({}, '没有此记录', 30002).response_json()
        else:
            data = ResumeProjectExperience.objects.filter(resume__id=resume_id, is_delete=False)
            return HandleResponse(data).response_json()

    def post(self, request):
        id = request.POST.get('id')
        resume_id = request.POST.get('resume_id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        name = request.POST.get('name')
        project_description = request.POST.get('project_description')
        responsibility_description = request.POST.get('responsibility_description')
        affiliated_company = request.POST.get('affiliated_company', None)

        if not all([resume_id, start_time, end_time, name, project_description, responsibility_description]):
            return HandleResponse({}, '参数错误', 20000).response_json()

        if id:
            ResumeProjectExperience.objects.filter(id=id).update(
                resume=Resume.objects.get(id=resume_id),
                start_time=start_time,
                end_time=end_time,
                name=name,
                project_description=project_description,
                responsibility_description=responsibility_description,
                affiliated_company=affiliated_company,
            )
            return HandleResponse({}, '修改成功').response_json()
        else:
            ResumeProjectExperience.objects.create(
                resume=Resume.objects.get(id=resume_id),
                start_time=start_time,
                end_time=end_time,
                name=name,
                project_description=project_description,
                responsibility_description=responsibility_description,
                affiliated_company=affiliated_company,
            )
            return HandleResponse({}, '添加成功').response_json()

    def delete(self, request):
        id = request.GET.get('id')

        if not all([id]):
            return HandleResponse({}, '参数错误', 20000).response_json()
        ResumeProjectExperience.objects.filter(id=id).update(is_delete=True)
        return HandleResponse({}, '删除成功').response_json()
