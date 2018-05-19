from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^$', views.blog_index,name='home'),
    url(r'^bloglist/$', views.blog_list,name='bloglist'),
    url(r'^blogdetails/(?P<pk>[0-9]+)/$', views.blog_details),
    url(r'^pre/(?P<pk>[0-9]+)/$', views.pre),
    url(r'^next/(?P<pk>[0-9]+)/$', views.next),
    url(r'^search$', views.search),

]
