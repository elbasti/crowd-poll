from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crowdpolls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pollresults.views.index'),
    url(r'success', TemplateView.as_view(template_name='pollresults/success.html')), 
    url(r'^admin/', include(admin.site.urls)),
)
