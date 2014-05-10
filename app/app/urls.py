from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ingledow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.about'),
    url(r'^blog/', include('blog.urls')),
    url(r'^work/', 'blog.views.work'),
    url(r'^contact/', 'blog.views.contact'),
)
