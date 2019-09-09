from django.conf.urls import url
from users.views import Test

urlpatterns = [
    url(r'^test$', Test.as_view(), name='test'),
]
