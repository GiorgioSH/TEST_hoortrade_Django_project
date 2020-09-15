# on configure correctement nos PATH avec nos URL, certains d'entre eux peuvent avoir un ID avec eux 
# on définit également le nom (name) de chacun afin de pouvoir rediriger les utilisateurs avec des url inclus dans des fichiers html 

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'myindex' ),
    path('acteur', views.acteur, name = 'page_acteur' ),
    path('apropos', views.apropos, name = 'page_apropos' ),
    path('realisateur', views.realisateur, name = 'page_realisateur' ),
    path('film', views.film, name = 'page_film' ),
    path('page_acteur/<str:pk_id>/', views.page_acteur, name = 'page_base_acteur' ),

    path('form_acteur/', views.creatActeur, name = 'form_acteur' ),
    path('form_acteur/<str:pk_id>/', views.updateActeur, name = 'form_acteur_update' ),
    path('delete_acteur/<str:pk_id>/', views.deleteActeur, name = 'delete_acteur' ),
]