
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tea'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^add/$', views.create_tea, name='tea-add'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.TeaUpdate.as_view(), name='tea-update'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.TeaDelete.as_view(), name='tea-delete'),

    # url(r'^(?P<tea_id>[0-9]+)/brew/(?P<pk>[0-9]+)/update/$', views.GongFuBrewUpdate.as_view(), name='gfbrew-update'),

    # url(r'^brew/(?P<pk>[0-9]+)/delete/$', views.GongFuBrewDelete.as_view(), name='gfbrew-delete'),

    url(r'^(?P<tea_id>[0-9]+)/add_brew/$', views.create_gfbrew, name='gfbrew-add'),

    url(r'^brew/(?P<pk>[0-9]+)/update/$', views.GongFuBrewUpdate.as_view(), name='gfbrew-update'),

    url(r'^brew/(?P<brew_id>[0-9]+)/delete/$', views.delete_gfbrew, name='gfbrew-delete'),



    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),

]
