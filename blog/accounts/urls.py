from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from accounts.views import RegistrationView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegistrationView.as_view(template_name='accounts/registration.html'), name='registration'),
]
