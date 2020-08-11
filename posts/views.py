from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from posts.forms import PostForm
from posts.models import Post


class PostView(View):
    template_name = None

    def get(self, request, author, pk):
        post = Post.objects.get(id=pk)
        form = None


        if request.user.is_authenticated and request.user == post.author:
            form = PostForm(instance=post)

        context = {
            'post': post,
            'form': form,
        }

        return render(request, self.template_name, context)

    
    def post(self, request, author, pk):
        post = Post.objects.get(id=pk)
        form = None


        if request.user.is_authenticated and request.user == post.author:
            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
        else:
            return redirect('home')

        context = {
            'post': post,
            'form': form,
        }

        return render(request, self.template_name, context)


class PostListView(ListView):
    model = Post


class PostListAuthorView(View):
    template_name = None

    def get(self, request, author):
        object_list = Post.objects.filter(author__username=author)

        return render(request, self.template_name, {'object_list': object_list})


class PostCreateView(View):
    template_name = None

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')

        context = {
            'form': PostForm()
        }

        return render(request, self.template_name, context)


    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('home')

        post = Post(author=request.user)
        form = PostForm(request.POST, instance=post)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
        else:
            return render(request, self.template_name, context)

        return redirect('home')
