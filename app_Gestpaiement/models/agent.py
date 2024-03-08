from django.db import models
from app_Gestpaiement.models.agent import *

class Agent(models.Model):
    agent = models.CharField(max_length=10, primary key=True)
    libelle = models.CharField(max_length=100)
