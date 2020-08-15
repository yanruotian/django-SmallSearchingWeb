from . import views, models
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.the_first_page),
    url(r'^echotest$', views.echo_test),
    url(r"^hello$", views.hello),
    url(r'^echo[/]{0,1}$', views.echo_introduce),
    url(r'^echo/(?P<string>.+)$', views.echo),
    url(r'^search$', views.search_test),
    url(r'^search/searching$', views.searching_test),
    url(r'^post_search$', views.post_test, name='search'),
]