from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

#Lists all blog post
def blog_list(request):
    posts = Blog.objects.all()
    query = request.GET.get("q")
    if query:
        posts = Blog.objects.filter(title__icontains=query)
    else:
        posts = Blog.objects.all()
    paginator = Paginator(posts,7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blog_list.html", {"all_blogs": posts, "page_obj": page_obj})

#Show details of single blog post
def blog_details(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/blog_details.html", {"details_of_blogs":post, "comments":comments, "form": form})

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk )
    if request.user != comment.author:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    if request.method == 'POST':
        form = CommentForm(request.POST, instance= comment)
        if form.is_valid():
            form.save()
            return redirect('blog_details', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    if request.method == 'POST':
        comment.delete()
        return redirect('blog_details', pk=comment.post.pk)
    return render(request, 'blog/delete_comment.html', {'comment':comment})


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

