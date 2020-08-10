from django import forms
from posts.models import Post


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'content')
