from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Lists all blog post
def blog_list(request):
    posts = Blog.objects.all()
    return render(request, "blog/blog_list.html", {"all_blogs": posts})

#Show details of single blog post
def blog_details(request, pk):
    posts = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/blog_details.html", {"details_of_blogs":posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) # include files for image upload
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author= request.user
            blog.save()
            messages.success(request, "Successfully uploaded the blog")
            return redirect('blog_list')
        else:
            messages.error(request,"There is some error while uploading the blog. Please check every field or try again!")
    else:
        form = BlogForm()
    return render(request, "blog/create_post.html", {"form":form})       
    
