from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'youku.views.main_page'),
    (r'^page/(\d{1,3})/$', 'youku.views.video_list_page'),
    (r'^video/(\d{4})/(\d{2})/(\d{2})/(\d{6})/$', 'youku.views.video_page'),
    (r'^log/(\d{1,3})/$', 'youku.views.log_page'),
    # admin related
    (r'^admin/', include(admin.site.urls)),
)
