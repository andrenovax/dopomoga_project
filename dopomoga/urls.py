from django.conf.urls import patterns, url
from dopomoga import views
# from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    # list
    url(r'^project_inneed_all/$', views.project_inneed_all, name='project_inneed_all'),
    url(r'^project_helper_all/$', views.project_helper_all, name='project_helper_all'),
    url(r'^userinneed_all/$', views.userinneed_all, name='userinneed_all'),
    url(r'^userhelper_all/$', views.userhelper_all, name='userhelper_all'),
    url(r'^resource_all/$', views.resource_all, name='resource_all'),
    url(r'^cause_all/$', views.cause_all, name='cause_all'),
    # items
    url(r'^project_helper_all/(?P<project_name_url>\w+)/$', views.project_helper_item, name='project_helper_item'),
    url(r'^project_inneed_all/(?P<project_name_url>\w+)/$', views.project_inneed_item, name='project_inneed_item'),
    url(r'^userhelper_all/(?P<user_name_url>\w+)/$', views.user_helper_item, name='user_helper_item'),
    url(r'^userinneed_all/(?P<user_name_url>\w+)/$', views.user_inneed_item, name='user_inneed_item'),
    url(r'^resource_all/(?P<resource_name_url>\w+)/$', views.resource_item, name='resource_item'),
    url(r'^cause_all/(?P<cause_name_url>\w+)/$', views.cause_item, name='cause_item'),
    # auth user
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # ajax
    url(r'^get_UserInneed/$', views.get_UserInneed, name='get_UserInneed'),
    url(r'^get_Resource/$', views.get_Resource, name='get_Resource'),
    url(r'^get_Cause/$', views.get_Cause, name='get_Cause'),
    url(r'^support_project/$', views.support_project, name='support_project'),
    )
