from django.conf.urls import url, include
from django.contrib import admin
from Login.views import login, login_auth, loggedin, invalid_login, logout, addPost, addPostAuth, editPost, editPostAuth, deletePostAuth

urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', login_auth),
    url(r'^logout/$', logout),
    url(r'^invalid/$', invalid_login),
    url(r'^admin/$', loggedin),
    url(r'^admin/addpost/$', addPost),
    url(r'^admin/addpost/auth$', addPostAuth),
    url(r'^admin/editpost/(?P<id>[0-9]+)/$', editPost),
    url(r'^admin/editpost/auth/(?P<id>[0-9]+)/$', editPostAuth),
    url(r'^admin/deletepost/(?P<id>[0-9]+)/$', deletePostAuth)
]
