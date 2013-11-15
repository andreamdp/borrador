from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from aplicacion.views import *
from aplicacion.vFicha import *
from aplicacion.forms import *
#from django.views.generic import list_detail, date_based, create_update

admin.autodiscover()

urlpatterns = patterns('',
   
    # Uncomment the next line to enable the admin:
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
 #   url('(?P<residenciaaut_id>\d+)/ficha/$', libro_pdf),
    url(r'(?P<residenciaaut_id>\d+)/ficha/$', reporteFicha),
    (r'reporte/2012/$', residencias2012),
    (r'reporte/2013/$', residencias2013),
	(r'^reporteA_evaluacion/$',aEvaluacion),
    
    url('', include(admin.site.urls)),
 #   (r'^basic-admin/', include(basic_site.urls)),
 #   (r'^advanced-admin/', include(advanced_site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
   
    # Your URL pattern could be as simple as
   
)
urlpatterns += patterns('',
                            (r'^grappelli/', include('grappelli.urls')),


)
