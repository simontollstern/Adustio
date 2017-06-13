from django.shortcuts import render, HttpResponse

from .models import BlogPosts

# Create your views here.

# Returns blog post data from the database as a string
def index(request):
    #all_blog_posts = BlogPosts.objects.all()
    return render(request, 'index.html', {
        'posts': BlogPosts.objects.all()
    })

    #return HttpResponse("<table><tr>" + p.post_title + " " + p.post_text + "</tr></table>" for p in all_blog_posts)
