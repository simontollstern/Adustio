from django.conf.urls import url, include
from django.contrib import admin
from Login.views import login, login_auth, loggedin, invalid_login, logout, addPost, addPostAuth

urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', login_auth),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/adminpanel/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login),
    url(r'^accounts/addpost/$', addPost),
    url(r'^accounts/addpost/auth$', addPostAuth)
]
