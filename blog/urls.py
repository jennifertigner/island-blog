from django.conf import settings
from django.conf.urls import include, url, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),  
  url(r'^$', views.index, name='index'),
  # these redirect to the homepage
  url(r'^article/$', RedirectView.as_view(pattern_name='index')),
  url(r'^articles/$', RedirectView.as_view(pattern_name='index')),
  url(r'^index/$', RedirectView.as_view(pattern_name='index')),
  url(r'^home/$', RedirectView.as_view(pattern_name='index')),
  url(r'^browse/$', RedirectView.as_view(pattern_name='index')), 
  # all the regular pages
  url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
  url(r'^browse/(?P<tag_word>[a-zA-Z]+)/$', views.browse, name='browse'),
  url(r'^search/$', views.search, name='search'),
  url(r'^about/$', views.about, name='about'), 
  url(r'^contact/$', views.contact, name='contact'),
  # error pages
  url(r'404/$', views.handler404),
  url(r'500/$', views.handler500),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
