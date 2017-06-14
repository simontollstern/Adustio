from django.conf.urls import url, include
from django.contrib import admin
from Login.views import login, auth_view, loggedin, invalid_login, logout, admin, addPost, addPostAuth

urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/adminpanel/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login),
    #url(r'^accounts/adminpanel/$', admin),
    url(r'^accounts/addpost/$', addPost),
    url(r'^accounts/addpost/auth$', addPostAuth)
]
