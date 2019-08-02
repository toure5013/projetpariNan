from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import userPari
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.sessions.models import Session

import logging
# from django.db import models
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'pari/index.html')


def parier(request):
    if request.method == 'GET':
        # On récupère les valeurs du formulaire
        montantparier = 3000
        if(montantparier is not None):
            first_name =  request.session['first_name']
            last_name =  request.session['last_name']
            username = request.session['user_name']
            numero = request.session['user_name']
            namePari = 'football'
            user_id = request.session['id']
            #Enregistrement dans la base 
            userpari = userPari(namePari=namePari, nameUser=first_name, montantParier=montantparier, datePari=datetime.now, idUser=user_id, status='gagné')
            userpari.save()
            user_id = request.user.id   
            user = User.objects.filter(id=user_id)
            return render(request,'pari/parier.html', {'user':user} )
    else:
        user_id = request.user.id   
        user = User.objects.filter(id=user_id)
        return render(request, 'pari/parier.html')


def profil(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        # récuperer les infos de l'utilisateur
        user = User.objects.filter(id=user_id)
        # userPariInfo = userPari.objects.get(idUser=user_id)
        # User.objects.get(username='john')
        return render(request,'pari/profil.html',{'user':user} )

    else:
        return redirect('connexion')


def connexion(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # //Recupération des donner de l'utilisateur depuis la Base
            data = User.objects.get(username=username)

            # //connexion de l'utilisateur            
            auth.login(request, user) 
            print('You are now logged in')

            # //envoi des donner à la session
            request.session['user_name'] = data.username
            request.session['first_name'] = data.first_name
            request.session['last_name'] = data.last_name
            request.session['email'] = data.email
            request.session['id'] = data.id

            # Renvoi sur la page de profil
            return redirect('profil')
        else:
            print('Données  non valide')
            return redirect('connexion')
    else:
        return render(request, 'pari/connexion.html')

def inscription(request):
    if request.method == 'POST':
        # On récupère les valeurs du formulaire
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        #username = request.POST['username']
        email = request.POST['email']
        numero = request.POST['numero']
        password = request.POST['password']
        password2 = request.POST['password2']

        # On vérifie si les password correspondent
        if password == password2:
            if User.objects.filter(email=email).exists():
                print("L'email existe déjà")
                return redirect('register')
            else:
                user = User.objects.create_user(username=numero, password=password,email=email, first_name=first_name, last_name=last_name)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                return redirect('connexion')
        else:
            print("Les mots de passes ne correspondent")
            return redirect('inscription')
    else:
        return render(request, 'pari/inscription.html')

def user_register(request):
   return render(request, 'pari/inscription.html')


# deconnexion

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')



# def basketball(request):
#     return render(request, 'pari/basketball.html')


# def handball(request):
#     return render(request, 'pari/handball.html')
 

# def football(request):
#     return render(request, 'pari/football.html')


# def dashbord(request):
#     return render(request, 'pari/dashbord.html')