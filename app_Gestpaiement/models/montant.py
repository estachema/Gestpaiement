from django.db import models

class Montant(models.Model):
    codeMontant = models.CharField(max_length=10,primary key=True)
    libelle = models.CharField(max_length=100)
