from django.urls import path
from posts.views import PostView
from posts.views import PostListView
from posts.views import PostListAuthorView
from posts.views import PostCreateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/create/new-post', PostCreateView.as_view(template_name='posts/post_create.html'), name='posts-create'),

    # Remember that there can be an author named create
    # This collides with the below urls
    path('posts/<str:author>/', PostListAuthorView.as_view(template_name='posts/post_list.html'), name='posts-author'),
    path('posts/<str:author>/<int:pk>/', PostView.as_view(template_name='posts/post.html'), name='posts-post'),

    # TODOOOOOOOO
    # path('posts/delete/<int:pk>/', PostDeleteView.as_view(template_name='posts/post_delete.html'), name='posts-delete'),
]
