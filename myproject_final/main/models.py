from django.db import models

# Nous allons créer des modèles qui vont représenter les tables de notre BDD

# Modèle : Acteur 
class Acteur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    age = models.IntegerField(max_length=20, null=True)
    description = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.nom

# Modèle : Réalisateur 
class Realisateur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    age = models.IntegerField(max_length=20, null=True)
    description = models.CharField(max_length=2000, null=True)
    
    def __str__(self):
        return self.nom

# Modèle : Film 
class Film(models.Model):
    AVIS = ( 
            ('Excellent film, je recommende','Excellent film je recommande'),
            ('Je ne le reverrai pas une deuxième fois','Je ne le reverrai pas une deuxième fois'),
            ('Je ne le conseillerai pas','Je ne le conseillerai pas'),
            )
    nom = models.CharField(max_length=200, null=True)
    Date_de_sortie = models.IntegerField(max_length=100, null=True)
    description = models.CharField(max_length=2000, null=True)
    # star = FloatField(null=True)
    avis = models.CharField(max_length=200, null=True, choices=AVIS)
    # Mise en relation de l'Acteur et du Réalisateur du film 
    # Acteur = 
    # Realisateur = 


    def __str__(self):
        return self.nom