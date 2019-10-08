from django.conf.urls import url
from base.views import AreaView, BannerView

urlpatterns = [
    url(r'^area$', AreaView.as_view(), name='area'),
    url(r'^banner$', BannerView.as_view(), name='banner'),
]
