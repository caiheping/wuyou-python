from django.contrib import admin
from companys.models import Companys, Job, Welfare


# Register your models here.


class CompanysAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'addr', 'introduce', 'personnel', 'company_start_time')

    search_fields = ('name', 'type')

    list_per_page = 50


class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'company', 'min_salary', 'max_salary', 'describe', 'working_years', 'education', 'recruitment')

    search_fields = ('job', 'education')

    list_per_page = 50


class WelfareAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_delete')

    search_fields = ('name',)

    list_per_page = 50


admin.site.register(Companys, CompanysAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Welfare, WelfareAdmin)
