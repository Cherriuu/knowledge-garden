from django.shortcuts import render

# Create your views here.
def index(request): # request this
    return render(request, 'learning_log/index.html') # renders index.html on webpage
