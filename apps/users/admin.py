from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy
from users.models import Users


# Register your models here.


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        (gettext_lazy('User Information'), {'fields': ('user', 'birthday', 'gender', 'mobile')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Users, UserAdmin)
