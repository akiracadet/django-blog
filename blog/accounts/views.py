from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import RegistrationForm


class RegistrationView(View):
    template_name = None

    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            logout(request)

        context = {
            'form': RegistrationForm()
        }

        return render(request, self.template_name, context)


    def post(self, request):
        context = {}

        if request.user.is_authenticated:
            logout(request)

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')

        context['form'] = form

        return render(request, self.template_name, context)


class ProfileView(View):
    template_name = None


    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')

        user_data = User.objects.get(pk=request.user.pk)
        context = {
            'user_data': {
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'email': user_data.email,
            },
        }

        return render(request, self.template_name, context)
