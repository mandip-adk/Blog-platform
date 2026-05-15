from django.forms import ModelForm, ClearableFileInput
from .models import Blog, Comment

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image"]
        widgets = {
            'image': ClearableFileInput(),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

