from django.shortcuts import render

def index(request):
    context = {'name': 'World'}  # Pass data to the template
    return render(request, 'lkApp/index.html', context)

def about(request):
    return render(request, 'lkApp/about.html')