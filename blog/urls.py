from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  # ex: /index
  url(r'^$', views.index, name='index'),
  # ex: /index
  url(r'^articles/$', RedirectView.as_view(url='views.index', permanent=False), name='index'),
  # ex: /articles/5
  url(r'^articles/(?P<article_id>[0-9]+)/$', views.articles, name='articles'),
  # ex: /articles/5/comment
  url(r'^articles/(?P<article_id>[0-9]+)/comment/$', views.comments, name='comments'),
  # ex: /browse
  url(r'^browse/$', views.browse, name='browse'), 
  # ex: /browse/beach
  url(r'^browse/(?P<tag_id>[a-zA-Z]+)/$', views.browse, name='browse'), 
  # ex: /about
  url(r'^about/$', views.about, name='about'), 
  # ex: /contact
  url(r'^contact/$', views.contact, name='contact'),
  # url(r'404/$', views.error404),
  # url(r'500/$', views.error500)
]
