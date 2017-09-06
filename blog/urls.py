from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.postpage, name='postpage'),
    url(r'^postproc$', views.postproc, name='postproc'),
    url(r'^comments$', views.comments, name='comments'),
    url(r'^logout_us$', views.logout_us, name='logout_us'),
    url(r'^login$', views.login, name='login'),
]
