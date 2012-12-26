from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from aplicacion.views import *
from aplicacion.forms import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Colegio.views.home', name='home'),
    # url(r'^Colegio/', include('Colegio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url('', include(admin.site.urls)),
 #   (r'^basic-admin/', include(basic_site.urls)),
 #   (r'^advanced-admin/', include(advanced_site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    (r'^admin/reporte/', my_view),
    # Your URL pattern could be as simple as
   
)
urlpatterns += patterns('',
                            (r'^grappelli/', include('grappelli.urls')),


)
