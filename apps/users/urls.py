from django.conf.urls import url
from users.views import Test, Login, Logout

urlpatterns = [
    url(r'^test$', Test.as_view(), name='test'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
]
