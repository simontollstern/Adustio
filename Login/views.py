from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from Blog.models import Post
from django import forms
from .forms import AddPostForm

# handles logins
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

# authenticates the logins
def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/adminpanel')
    else:
        return HttpResponseRedirect('/accounts/invalid')

# happens if login isnt authenticated
def invalid_login(request):
    return render(request, 'invalid_login.html')

#Pages where you are required to be logged in to access them
@login_required()
def loggedin(request):
    return render(request, 'adminpanel.html', {
            'full_name': request.user.username,
            'posts': Post.objects.all().order_by("pk"),
        })

@login_required()
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

#@login_required()
#def admin(request):
#    return HttpResponseRedirect('/accounts/adminpanel')

@login_required()
def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/accounts/addpost')
    else:
        form = AddPostForm()

    return render(request, 'addpost.html', {'form': form})

@login_required()
def addPostAuth(request):
    title = request.POST.get('title', '')
    text = request.POST.get('text', '')
    date = request.POST.get('date', '')

    p = Post(title=title, text=text, date=date)
    p.save()

    return HttpResponseRedirect('/accounts/adminpanel')

#@login_required()
#def deletePost(request):

@login_required()
def deletePostAuth(request, id):
    Post.objects.get(pk=id).delete()

    return HttpResponseRedirect('/accounts/adminpanel')
