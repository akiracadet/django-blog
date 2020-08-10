from django.urls import path
from posts.views import PostView
from posts.views import PostListView
from posts.views import PostListAuthorView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<str:author>/', PostListAuthorView.as_view(template_name='posts/post_list.html'), name='posts-author'),
    path('posts/<str:author>/<int:pk>/', PostView.as_view(template_name='posts/post.html'), name='posts-post'),
]
