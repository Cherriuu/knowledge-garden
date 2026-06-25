from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def logout_view(request):
    # logs the user out using djangos logout function
    logout(request)
    return HttpResponseRedirect(reverse('learning_log:index'))
