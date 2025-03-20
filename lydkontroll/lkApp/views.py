from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required #if you want only logged in users to access this.

def index(request):
    context = {'name': 'World'}  # Pass data to the template
    return render(request, 'lkApp/index.html', context)

def about(request):
    return render(request, 'lkApp/about.html')

def indexLogin(request):
    return render(request, 'lkApp/indexLogin.html')


@login_required #add this if you want only logged in users to access this.
def profile(request):
    return render(request, 'lkApp/indexLogin.html') #create a profile.html template.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('indexLogin')  # Redirect to your index page
    else:
        form = RegisterForm()
    return render(request, 'lkApp/register.html', {'form': form})