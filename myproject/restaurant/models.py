from django.db import models
from django.contrib.auth.models import User 


# Create your models here.


class Menu (models.Model):
    nom        = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    type        = models.CharField(max_length=30)
    nb_table    = models.TextField(max_length=10)
    
    def __str__(self):
        return self.nom


class Product (models.Model):
    categorie   = models.CharField(max_length=50, unique=True)
    type        = models.CharField(max_length=30)
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE,
                                    related_name='products'
                                    )
                                    


class Choice (models.Model):
    nom        = models.CharField(max_length=30, unique=True)
    composition = models.CharField(max_length=100)
    prix        = models.IntegerField()
    
class Commande (models.Model):
    composition = models.TextField(max_length=1000)
    prix        = models.IntegerField()
    nb_commande  = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='commandes'
                                     )
    
class Utilisateur (models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE,
                                 related_name='Utilisateurs'
                                )
    table    = models.ForeignKey(Menu, on_delete=models.CASCADE,
                                 related_name='Utilisateurs'
                                 )

    