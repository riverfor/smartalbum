from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^$', 'album.views.home', name='Album Home'),
     url(r'^detail/(\d+)$', 'album.views.detail', name='Album Detail'),
)
