from django.contrib import admin
from resumes.models import Resume, ResumeEducation, ResumeJob, ResumeProjectExperience, ResumeWorking


# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'progress', 'user', 'is_open')

    search_fields = ('username', 'name')

    list_per_page = 50


class ResumeWorkingAdmin(admin.ModelAdmin):
    list_display = ('resume', 'start_time', 'end_time', 'company', 'position')

    list_per_page = 50


class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ('resume', 'enrollment_time', 'graduation_time', 'school', 'education', 'major', 'is_overseas_study')

    search_fields = ('school', 'education')

    list_per_page = 50


class ResumeJobAdmin(admin.ModelAdmin):
    list_display = ('resume', 'place', 'function', 'pay_type', 'salary_expectation', 'work_type', 'industry', 'arrival_time')

    list_per_page = 50


class ResumeProjectExperienceAdmin(admin.ModelAdmin):
    list_display = ('resume', 'start_time', 'end_time', 'name')

    search_fields = ('name',)

    list_per_page = 50


admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeWorking, ResumeWorkingAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
admin.site.register(ResumeJob, ResumeJobAdmin)
admin.site.register(ResumeProjectExperience, ResumeProjectExperienceAdmin)
