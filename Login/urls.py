from django.conf.urls import url, include
from django.contrib import admin
from Login.views import login, login_auth, loggedin, invalid_login, logout, addPost, addPostAuth, editPost, editPostAuth, deletePostAuth

urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', login_auth),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/invalid/$', invalid_login),
    url(r'^accounts/adminpanel/$', loggedin),
    url(r'^accounts/adminpanel/addpost/$', addPost),
    url(r'^accounts/adminpanel/addpost/auth$', addPostAuth),
    url(r'^accounts/adminpanel/editpost/(?P<id>[0-9]+)/$', editPost),
    url(r'^accounts/adminpanel/editpost/auth/(?P<id>[0-9]+)/$', editPostAuth),
    url(r'^accounts/adminpanel/deletepost/(?P<id>[0-9]+)/$', deletePostAuth)
]
