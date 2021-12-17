from django.contrib.auth import login, authenticate, logout
from django.http import request
from .forms import ProfilForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def index(request):
    return render(request, 'chat/index.html', {})

@login_required(login_url = 'login')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def register(request):
    form = ProfilForm()
    if request.method == 'POST':
        form = ProfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            return render(request,'chat/register.html', {'form':form})
    else:
        return render(request, 'chat/register.html', {'form':form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"Ulogovan korisnik {user.get_username()}")
            return redirect(index)
        else:
            return redirect(index)            
    return render(request, 'chat/login.html')

def logoutPage(request):
    logout(request)
    return redirect(loginPage)