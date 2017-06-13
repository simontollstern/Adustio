from django.http import HttpResponse

from .models import BlogPosts

# Create your views here.
def index(request):
    return HttpResponse("Root page")

# Returns blog post data from the database as a string
def displayBlogPosts(request):
    all_blog_posts = BlogPosts.objects.all()
    
    return HttpResponse("<table><tr>" + p.post_title + " " + p.post_text + "</tr></table>" for p in all_blog_posts)
