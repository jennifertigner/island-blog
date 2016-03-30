from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  # this is the homepage (localhost:8000)
  url(r'^$', views.index, name='index'),
  # these redirect to the homepage
  url(r'^article/$', RedirectView.as_view(pattern_name='index')),
  url(r'^index/$', RedirectView.as_view(pattern_name='index')),
  url(r'^home/$', RedirectView.as_view(pattern_name='index')),
  # ex: /articles/5
  url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
  # ex: /browse
  url(r'^browse/$', views.browse_tag_list, name='browse_tag_list'), 
  # ex: /browse/beach
  url(r'^browse/(?P<tag_id>[a-zA-Z]+)/$', views.browse, name='browse'), 
  # ex: /about
  url(r'^about/$', views.about, name='about'), 
  # ex: /contact
  url(r'^contact/$', views.contact, name='contact'),
  # url(r'404/$', views.error404),
  # url(r'500/$', views.error500)
]
