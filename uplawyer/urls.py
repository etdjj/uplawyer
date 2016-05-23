from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sflawyer.views.home', name='home'),
    url(r'^about/(\w+)$', 'sflawyer.views.about', name='about'),
    url(r'^team$', 'sflawyer.views.team', name='team'),
    url(r'^part', 'sflawyer.views.part', name='part'),
    url(r'^join', 'sflawyer.views.jion', name='jion'),
    url(r'^book/(\d*)$', 'sflawyer.views.book', name='book'),
    url(r'^news/(\d*)$', 'sflawyer.views.news', name='news'),
    url(r'^human/(\d*)$', 'sflawyer.views.human', name='human'),
    url(r'^paper$', 'sflawyer.views.paper', name='paper'),
    url(r'^good', 'sflawyer.views.good', name='good'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
)
