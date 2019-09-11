from django.contrib import admin
from base.models import Banner, AreaInfo

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('index', 'image', 'url')

    list_per_page = 50


class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'atitle', 'aParent')

    search_fields = ('atitle',)

    ordering = ('id',)

    list_per_page = 50


admin.site.register(Banner, BannerAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)
