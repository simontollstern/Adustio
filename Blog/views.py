from django.shortcuts import render, HttpResponse
from Blog.models import Post
from datetime import datetime
from django.utils import timezone

# Create your views here.

# Returns blog post data from the database as a string
def index(request):
    months = []
    for m in Post.objects.all().order_by('-date'):
        if m.date.strftime("%B%y") not in months:
            months.append(m.date.strftime("%B%y"))
    return render(request, 'index.html', {
        'posts': Post.objects.all().order_by('-date'),
        'months': months,
    })

# For viewing all posts from a specific year entered in the URL
def post_year(request, year):
    #datetime_object = datetime.strptime('2016-08-02 10:14:00.000000', '%Y-%m-%d %H:%M:%S.%f')
    return render(request, 'post.html', {
        'postDates': Post.objects.filter(date__year=year).order_by('-date')
    })
# For viewing all posts from a specific year and month entered in the URL
def post_month(request, year, month):
    return render(request, 'post.html', {
        'postDates': Post.objects.filter(date__year=year, date__month=month).order_by('-date')
    })
# For viewing all posts from a specific year, month and date entered in the URL
def post_day(request, year, month, day):
    return render(request, 'post.html', {
        'postDates': Post.objects.filter(date__year=year, date__month=month, date__day=day).order_by('-date')
    })
