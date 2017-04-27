from django.conf.urls import url

from . import views

app_name = "myapp"

urlpatterns = [
    # ex: /myapp/
    url(r'^index', views.index, name='index'),
    url(r'^user/(?P<player_id>[0-9]+)/$', views.user, name='user'),
]