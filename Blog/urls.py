from django.conf.urls import url, include
from Blog.views import post_year, post_month, post_day

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]+)/$', post_year),
    url(r'^blog/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', post_month),
    url(r'^blog/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', post_day)
]
