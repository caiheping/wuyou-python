from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Users


# Register your models here.


class UserProfileAdmin(UserAdmin):
    # 设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('username', 'last_login', 'is_superuser', 'is_staff', 'area', 'is_active')

    search_fields = ('username',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50


admin.site.register(Users, UserProfileAdmin)
