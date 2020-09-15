# Création de formulaire avec le modèle/classe python

# Nous allons utiliser la "création" et le "Update" avec ce formulaire
from django.forms import ModelForm 
from .models import *

class ActeurForm(ModelForm):
    class Meta:
        model = Acteur
        fields = '__all__'

