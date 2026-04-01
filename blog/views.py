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
    
@login_required
def edit_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully uploaded the blog")
            return redirect('blog_list')
        else:
           messages.error(request, "There was an error updating the blog. Please check the fields.")
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form , 'blog': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog_list')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('blog_list')

    return render(request, 'blog/delete_post.html', {'post': post})

