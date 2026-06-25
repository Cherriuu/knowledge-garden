from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def logout_view(request):
    # logs the user out using djangos logout function
    logout(request)
    return HttpResponseRedirect(reverse('learning_log:index'))

def register(request):
    # register a new user
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect them to the homepage
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            return HttpResponseRedirect(reverse('learning_log:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

    
