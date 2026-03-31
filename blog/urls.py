from django.urls import path, include
from .views import blog_details, blog_list, create_post
from .apiviews import BlogViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"post", BlogViewSet)

urlpatterns = [
    path("blog_details/<int:pk>/", blog_details, name="blog_details"),
    path("blog_list/", blog_list, name= "blog_list" ),
    path("create_post/", create_post, name= "post"),
    #For API
    path("", include(router.urls)),
    

]






