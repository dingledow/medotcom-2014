from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('',
        url(r'^$', 'blog.views.index'),
        url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    )
