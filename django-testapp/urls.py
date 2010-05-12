from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'youku.views.main_page'),
    (r'^page/(\d{1,3})/$', 'youku.views.video_list_page'),
    # admin related
    (r'^admin/', include(admin.site.urls)),
)
