from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView , PasswordChangeView , LoginView
from .forms import CustomUserCreationForm , CustomUserChangeForm 
from .models import CustomUser
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')