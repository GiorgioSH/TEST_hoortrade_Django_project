# Ici on regarde définit les objets view et on leur attribue un ensemble d'éléments qu'ils vont récupérer via les Modèles, 
# on définit vers quels fichiers ils vont pointer et quelles données ils vont transmettre

from django.shortcuts import render, redirect
from .models import *
from .form import ActeurForm

# from django.http import HttpResponse

# Create your views here.

# request : contient des info sur la requête : type get, post, data sur l'utilisateur ..
def index (request):  
    # return HttpResponse('HEY')
    acteurs = Acteur.objects.all()
    total_acteurs = acteurs.count()

    films = Film.objects.all()
    total_films = films.count()

    realisateurs = Realisateur.objects.all()
    total_realisateurs = realisateurs.count()

    context = { 'acteurs':acteurs,'films':films,
    'realisateurs':realisateurs,'total_acteurs':total_acteurs,
    'total_films':total_films,'total_realisateurs':total_realisateurs}
    
    return render(request,'home/index.html', context)

def acteur (request):
    acteurs = Acteur.objects.all()
    return render(request,'home/acteur.html', {'acteurs':acteurs})

def apropos (request):
    return render(request,'home/apropos.html')
    
def realisateur (request):
    mes_realisateur = Realisateur.objects.all()
    
    context = { 'realisateur':realisateur,'mes_realisateur':mes_realisateur,}
    return render(request,'home/realisateur.html', context)

def film (request):
    mes_films = Film.objects.all()
    
    context = { 'film':film,'mes_films':mes_films,}
    return render(request,'home/film.html', context)

def page_acteur (request, pk_id):
    mes_acteurs = Acteur.objects.get(id=pk_id)
    
    context = { 'acteur':acteur,'mes_acteurs':mes_acteurs,}

    return render(request,'home/page_base_acteur.html', context)

def creatActeur(request):

    form = ActeurForm()
    if request.method == 'POST': 
        form = ActeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_acteur')


    context = {'form':form}
    return render(request,'home/form_acteur.html', context)
    
def updateActeur(request, pk_id):
    acteurs = Acteur.objects.get(id=pk_id)

    # myacteur = Acteur.objects.get(id=pk_id)
    
    # mes_acteurs = Acteur.objects.get(id=pk_id)
    form = ActeurForm(instance=acteurs)

    if request.method == 'POST':
        form = ActeurForm(request.POST, instance=acteurs)
        if form.is_valid():
            form.save()
            return redirect('page_acteur')

    context = {'form':form,'acteurs':acteurs}
    return render(request,'home/form_acteur.html', context)

def deleteActeur(request, pk_id):
    acteurs = Acteur.objects.get(id=pk_id)
    if request.method == "POST":
        acteurs.delete()
        return redirect('page_acteur')
    context = {'item':acteurs}
    return render(request,'home/delete.html', context)