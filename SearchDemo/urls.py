from . import views, models
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<id>[0-9]+)$', views.show_by_id, name='details'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]