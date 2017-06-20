from django.shortcuts import render, HttpResponse
from Blog.models import Post
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Returns blog post data from the database as a string
def index(request):
    months = []
    for m in Post.objects.all().order_by('-date'):
        if m.date.strftime("%B%y") not in months:
            months.append(m.date.strftime("%B%y"))

    post_list = Post.objects.all().order_by('-date')
    paginator = Paginator(post_list, 5, orphans=1)

    page =request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {
        'posts': posts,
        'months': months,
    })

# For viewing all posts from a specific year entered in the URL
def post_year(request, year):
    return render(request, 'blog/post.html', {
        'posts': Post.objects.filter(date__year=year).order_by('-date')
    })
# For viewing all posts from a specific year and month entered in the URL
def post_month(request, year, month):
    return render(request, 'blog/post.html', {
        'posts': Post.objects.filter(date__year=year, date__month=month).order_by('-date')
    })
# For viewing all posts from a specific year, month and date entered in the URL
def post_day(request, year, month, day):
    return render(request, 'blog/post.html', {
        'posts': Post.objects.filter(date__year=year, date__month=month, date__day=day).order_by('-date')
    })
