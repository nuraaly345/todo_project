from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import ToDo

def home(request):
    return render(request, 'todoapp/home.html')

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

def loginuser(request):
    if request.method == 'GET':
        return render(request, "todoapp/loginuser.html", {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "todoapp/loginuser.html", {'form': AuthenticationForm() , 'error': 'Колдонуучунун аты жана сыр соз табылган жок'})
        else:
            login(request, user)
            return redirect('currenttodos')



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todoapp/createtodo.html', {'form':TodoForm() })
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todoapp/createtodo.html', {'form': TodoForm(), 'error': 'Жазууда ката кетти. Кайрадан аракет кылыңыз'})


def viewtodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todoapp/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todoapp/viewtodo.html', {'todo': todo, 'form':form, 'error': 'Маалымат туура эмес жазылды'})

def currenttodos(request):
    todos = ToDo.objects.filter(user = request.user, completed__isnull=True)
    return render(request, 'todoapp/current.html', {'todos': todos})

