from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images/" , null=True, blank=True)


class Comment(models.Model):

    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
     