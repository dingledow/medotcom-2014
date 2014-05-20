from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

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

    #redirects
    url(r'^blog//puma-social-club/', RedirectView.as_view(url='http://david.ingledow.co.uk/blog/puma-social-club/', permanent=True)),
    url(r'^blog//apples-leather-iphone-case/', RedirectView.as_view(url='http://david.ingledow.co.uk/blog/apples-leather-iphone-case/', permanent=True)),
    url(r'^blog//git-awesome-design-tool/', RedirectView.as_view(url='http://david.ingledow.co.uk/blog/git-awesome-design-tool/', permanent=True)),
    url(r'^blog//canniest-degree-show-earth/', RedirectView.as_view(url='http://david.ingledow.co.uk/blog/canniest-degree-show-earth/', permanent=True)),
    url(r'^orbis', RedirectView.as_view(url='http://david.ingledow.co.uk/work/orbis/', permanent=True)),
)
