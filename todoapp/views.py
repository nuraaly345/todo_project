from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):

    return render(request, "todoapp/signupuser.html", {'form': UserCreationForm() })
