from django.conf.urls import url
from base.views import GetArea, GetBanner

urlpatterns = [
    url(r'^get_area$', GetArea.as_view(), name='get_area'),
    url(r'^get_banner$', GetBanner.as_view(), name='get_banner'),
]
