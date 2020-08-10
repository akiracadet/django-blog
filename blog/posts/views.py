from django.shortcuts import redirect, render
from django.views.generic import ListView
from posts.models import Post


class PostListView(ListView):
    model = Post


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = Post.objects.filter(author=self.request.user)
        context['object_list'] = posts

        return context


    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')

        return super().get(request)
