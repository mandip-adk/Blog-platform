from django.urls import path, include
from .views import registration

urlpatterns=[
    path('register/',registration, name="register" ),
    
]