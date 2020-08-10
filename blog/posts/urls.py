from django.urls import path
from posts.views import PostListView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts')
]