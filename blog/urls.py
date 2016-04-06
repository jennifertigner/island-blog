from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

# from django.conf.urls import (
#     handler400, handler403, handler404, handler500
# )

# handler400 = 'views.handler400'
# handler403 = 'views.handler403'
# handler404 = 'views.handler404'
# handler500 = 'views.handler500'

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^markdownx/', include('markdownx.urls')),
  # this is the homepage (localhost:8000)
  url(r'^$', views.index, name='index'),
  # these redirect to the homepage
  url(r'^article/$', RedirectView.as_view(pattern_name='index')),
  url(r'^articles/$', RedirectView.as_view(pattern_name='index')),
  url(r'^index/$', RedirectView.as_view(pattern_name='index')),
  url(r'^home/$', RedirectView.as_view(pattern_name='index')),
  url(r'^browse/$', RedirectView.as_view(pattern_name='index')), 
  # ex: /articles/5
  url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
  # ex: /browse/Beach
  url(r'^browse/(?P<tag_word>[a-zA-Z]+)/$', views.browse, name='browse'),
  # ex: /about
  url(r'^about/$', views.about, name='about'), 
  # ex: /contact
  url(r'^contact/$', views.contact, name='contact'),
  # error pages
  url(r'404/$', views.handler404),
  url(r'500/$', views.handler500),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


