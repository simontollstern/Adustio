from django.shortcuts import render_to_response, render
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
    return render_to_response('login.html', c)

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
    return render_to_response('invalid_login.html')

#Pages where you are required to be logged in to access them
@login_required()
def loggedin(request):
    return render_to_response('adminpanel.html', {
            'full_name': request.user.username,
            'posts': Post.objects.all().order_by("pk"),
        })

@login_required()
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

#@login_required()
#def admin(request):
#    return HttpResponseRedirect('/accounts/adminpanel')

@login_required()
def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
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


#@login_required()
#def deletePostAuth(request):

# Returns blog post data from the database as a string
"""def index(request):
    months = []
    for m in Post.objects.all().order_by('-date'):
        if m.date.strftime("%B%y") not in months:
            months.append(m.date.strftime("%B%y"))
    return render(request, 'adminpanel.html', {
        'posts': Post.objects.all().order_by('-date'),
        'months': months,
    })"""