from django.shortcuts import render, redirect
from django. contrib import messages
from django.contrib.auth import views as authentication_views
from .serializer import ProfileSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .register_form import RegisterForm
from .models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}. Your account is created successfully!")
            return redirect('login')
    else:
        form = RegisterForm(request.POST)

    return render(request, 'user_app/register.html', {'form':form})

class CustomLoginView(authentication_views.LoginView):
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Logged in as {username}')
        return super().form_valid(form)

@login_required
def profilepage(request):
    return render (request, 'user_app/profile.html')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer