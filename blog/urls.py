from django.urls import path, include
from .views import blog_details, blog_list, create_post, edit_post, delete_post
from .apiviews import BlogViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"post", BlogViewSet)

urlpatterns = [
    path("blog_details/<int:pk>/", blog_details, name="blog_details"),
    path("blog_list/", blog_list, name= "blog_list" ),
    path("create_post/", create_post, name= "post"),
    path("blog/post/<int:pk>/edit/", edit_post, name="edit_post"),
    path("blog/post/<int:pk>/delete", delete_post, name= "delete_post"),
    #For API
    path("", include(router.urls)),
    

]






