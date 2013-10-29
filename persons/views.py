from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import persons.forms as personform


def loginuser(request):
    if request.method == 'POST':
        form = personform.LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            u = authenticate(username=name, password=password)
            if u is not None:
                if u.is_active:
                    login(request, u)
                else:
                    msj = 'lo sentimos este usuario no se encuntra disponible'
                return redirect('/')
            else:
                return redirect('person/login.html')
    else:
        form = personform.LoginForm()
    return render(request, 'persons/login.html', {'form': form})


def registeruser(request):
    if request.method == 'POST':
        pass
    else:
        form = personform.RegisterForm()
    return render(request, 'persons/register.html', {'form': form})




def logoutuser(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('home')
