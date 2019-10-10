from django.conf.urls import url
from companys.views import CompanysView, JobView, WelfareView

urlpatterns = [
    url(r'^companys$', CompanysView.as_view(), name='companys'),
    url(r'^job$', JobView.as_view(), name='job'),
    url(r'^welfare$', WelfareView.as_view(), name='welfare'),
]
