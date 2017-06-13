from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

# Returns blog post data from the database as a string
def index(request):
    return render(request, 'index.html', {
        'posts': Post.objects.all()
    })
