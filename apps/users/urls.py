from django.conf.urls import url
from users.views import Login, Logout

urlpatterns = [
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
]
