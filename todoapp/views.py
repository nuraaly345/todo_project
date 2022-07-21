from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signup(request):
    if request.method == 'GET':
        return render(request, "todoapp/signupuser.html", {'form': UserCreationForm() })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, "todoapp/signupuser.html", {'form': UserCreationForm(), 'error': 'Мындай колдонуучу тузүлгөн. Башка жаңы ат жазыңыз' })
        else:
            return render(request, "todoapp/signupuser.html", {'form': UserCreationForm(), 'error': 'Сыр сөз дал келбей калды' })


def currenttodos(request):
    return render(request, 'todoapp/current.html')