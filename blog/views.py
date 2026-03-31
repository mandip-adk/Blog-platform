from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm

#Lists all blog post
def blog_list(request):
    posts = Blog.objects.all()
    return render(request, "blog/blog_list.html", {"all_blogs": posts})

#Show details of single blog post
def blog_details(request, pk):
    posts = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/blog_details.html", {"details_of_blogs":posts})

