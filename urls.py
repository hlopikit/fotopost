# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

to_static = lambda req: HttpResponsePermanentRedirect('/static'+req.path)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)