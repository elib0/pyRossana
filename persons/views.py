#encoding:utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import persons.forms as personform
from django.contrib.auth.models import User
from persons.models import PromoterPhotos
from django.utils import simplejson
from django.http import HttpResponse


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
                    # msj = 'lo sentimos este usuario no se encuntra disponible'
                    pass
                return redirect('/')
            else:
                return redirect('person/login.html')
    else:
        form = personform.LoginForm()
    return render(request, 'persons/login.html', {'form': form})


def registeruser(request):
    if request.is_ajax() and request.method == 'POST':
        result = {'success': -1, 'message': 'Error desconocido'}
        form = personform.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            u = User.objects.create_user(username, email, password)
            try:
                u.save()
                result['success'] = 1
                result['message'] = '¡Usuario creado correctamente!'
            except:
                result['success'] = 0
                result['message'] = 'Ah ocurrido un error al intentar crear el usuario!'
        json = simplejson.dumps(result)
        return HttpResponse(json, mimetype='application/json')
    else:
        form = personform.RegisterForm()
    return render(request, 'persons/register.html', {'form': form})


def logoutuser(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('home')


def profile(request):
    u = request.user
    user_data = {'first_name': u.first_name,
                 'last_name': u.last_name, 'email': u.email}
    # if u.buyer in locals():
        # pass

    profileform = personform.ProfileForm(user_data)
    passform = personform.ChangePasswordForm()
    return render(request, 'persons/profile.html', {'profileform': profileform,
                                                    'passform': passform})


def ajax_change_password(request):
    if request.is_ajax():
        pass


def ajax_update_profile(request):
    if request.is_ajax() and request.method == 'POST':
        result = {'success': -1, 'message': 'Error desconocido'}
        form = personform.ProfileForm(request.POST)
        u = request.user
        if form.is_valid():
            u.first_name = form.cleaned_data['first_name']
            u.last_name = form.cleaned_data['last_name']
            u.email = form.cleaned_data['email']
            try:
                request.user.save()
                result['success'] = 1
                result['message'] = '¡Se han actualizado sus datos!'
            except:
                result['success'] = 0
                result['message'] = 'Ah ocurrido un error al intentar actualizar!'
        json = simplejson.dumps(result)
        return HttpResponse(json, mimetype='application/json')


def registerpromoter(request):
    if request.is_ajax():
        if request.method == 'POST':
            form = personform.PromoterForm(request.POST, request.FILES)
            if form.is_valid():
                p = form.save()
                pp = PromoterPhotos(promoter=p,
                                    photo1=form.cleaned_data['photo1'],
                                    photo2=form.cleaned_data['photo2'])
                pp.save()
        else:
            form = personform.PromoterForm()
        return render(request, 'persons/register_promoter.html',
                      {'form': form})
