from . import views
from django.urls import path

urlpatterns = [
    path('', views.add_post, name='addpost'),
]