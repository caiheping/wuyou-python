from django.conf.urls import url
from companys.views import CompanysView

urlpatterns = [
    url(r'^companys$', CompanysView.as_view(), name='companys'),
]
