from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

# Returns blog post data from the database as a string
def index(request):
    return render(request, 'index.html', {
        'posts': Post.objects.all()
    })

    #all_blog_posts = BlogPosts.objects.all()
    #return HttpResponse("<table><tr>" + p.post_title + " " + p.post_text + "</tr></table>" for p in all_blog_posts)
