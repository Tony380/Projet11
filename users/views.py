from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfile, ModifyUsername
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User


def register(request):
    """ User registration function """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request,
                             'Bienvenu! Votre compte a été créé avec succès ! '
                             'Vous êtes maintenant connecté')
            login(request, user)
            return redirect('index')
        else:
            form = RegisterForm(request.POST)
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    """ User's profile page """
    return render(request, 'profile.html')


class LoginFormView(SuccessMessageMixin, LoginView):
    """ Add a welcome message when user logs in """
    success_message = "Bienvenu! Vous êtes maintenant connecté"


class PasswordView(SuccessMessageMixin, PasswordChangeView):
    """ Add a success message when user modifies his password """
    success_message = "Votre mot de passe a été modifié avec succès !"


@login_required
def logout_view(request):
    """ User logout function """
    logout(request)
    messages.success(request, 'Au revoir! Vous êtes maintenant déconnecté')
    return redirect('index')


@login_required
def update(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            User.objects.filter(id=request.user.id).update(
                email=form.cleaned_data.get('email'))
            User.objects.filter(id=request.user.id).update(
                first_name=form.cleaned_data.get('first_name'))
            User.objects.filter(id=request.user.id).update(
                last_name=form.cleaned_data.get('last_name'))
            messages.success(request,
                             'Votre profil a été mis à jour avec succès !')
            return redirect('users:profile')
        else:
            form = UpdateProfile()
            return render(request, 'update.html', {'form': form})

    else:
        form = UpdateProfile()
        return render(request, 'update.html', {'form': form})


@login_required
def modify_username(request):
    if request.method == 'POST':
        form = ModifyUsername(request.POST)
        if form.is_valid():
            User.objects.filter(id=request.user.id).update(
                username=form.cleaned_data.get('username'))
            messages.success(request,
                             "Votre nom d'utilisateur a été mis à jour avec succès !")
            return redirect('users:profile')
        else:
            messages.success(request,
                             "Ce nom d'utilisateur existe déjà !")
            form = ModifyUsername()
            return render(request, 'username.html', {'form': form})

    else:
        form = ModifyUsername()
        return render(request, 'username.html', {'form': form})


@login_required
def del_user(request):
    user = request.user
    logout(request)
    user.delete()
    messages.success(request, "Votre profil a été supprimé avec succès !")
    return redirect('index')
