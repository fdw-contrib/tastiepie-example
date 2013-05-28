from django.conf.urls import patterns, include, url
from restful_app.api import PersonResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

person_resource = PersonResource()

urlpatterns = patterns('',
    (r'^api/', include(person_resource.urls)),
    # Examples:
    # url(r'^$', 'restful_example.views.home', name='home'),
    # url(r'^restful_example/', include('restful_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
