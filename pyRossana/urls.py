from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pyRossana.views.home', name='home'),
    # url(r'^pyRossana/', include('pyRossana.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', include('store.urls', namespace="store")),
    url(r'^persons/', include('persons.urls', namespace="person")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
