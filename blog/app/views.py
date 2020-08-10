from django.shortcuts import redirect, render
from django.views import View


class HomeView(View):
    template_name = 'app.html'


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts')


        return render(request, self.template_name)
