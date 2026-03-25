from django.urls import path, include
from .views import blog_details, blog_list
from .apiviews import BlogViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"post", BlogViewSet)

urlpatterns = [
    path("blog_details/<int:pk>/", blog_details, name="blog_details"),
    path("blog_list/", blog_list, name= "blog_list" ),

    #For API
    path("", include(router.urls)),
    

]






