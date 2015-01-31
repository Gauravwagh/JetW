from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import os
from settings import OUR_APPS, DEBUG, MEDIA_ROOT, BASE_DIR


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'task.views.home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    
)
  
for app in OUR_APPS:
    urlpatterns += patterns('', url(r'^' + app + '/', include(app + '.urls', app_name=app)),)

if DEBUG:
    urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root':MEDIA_ROOT}),
                        )
# To provide admin UI on server this is static url

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(BASE_DIR, 'templates/static')}),

                    )