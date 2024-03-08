from django.db import models
from app_Gestpaiement.models.montant import *

class Montant(models.Model):
    montant = models.CharField(max_length=10, primary key=True)
    libelle = models.CharField(max_length=100)
