from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', 'views.hello'),
    (r'^datetime/$', 'views.current_datetime'),
    (r'^datetime/plus/(\d{1,2})/$', 'views.hours_ahead'),
    (r'^meta/$', 'views.display_meta'),
    (r'^search/$', 'books.views.search'),
    (r'^contact/$', 'contact.views.contact'),
    (r'^youku/$', 'views.best_of_youku'),
    (r'^$', 'youku.views.main_page'),
    (r'^admin/', include(admin.site.urls)),
)
