from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from Blog.models import Post
from django import forms
from .forms import PostForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/adminpanel')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def invalid_login(request):
    return render_to_response('invalid_login.html')

@login_required()
def loggedin(request):
    return render_to_response('adminpanel.html', {'full_name': request.user.username})

@login_required()
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

@login_required()
def admin(request):
    return HttpResponseRedirect('/accounts/adminpanel')

@login_required()
def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/accounts/addpost')
    else:
        form = PostForm()

    return render(request, 'addpost.html', {'form': form})

@login_required()
def addPostAuth(request):
    title = request.POST.get('title', '')
    text = request.POST.get('text', '')

    b = Post(title=title, text=text)
    b.save()

    return HttpResponseRedirect('/accounts/adminpanel')
