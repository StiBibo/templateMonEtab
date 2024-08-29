from django.db import models

# Create your models here.



class Eleve(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sexe = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    classe = models.CharField(max_length=255)
    date_naissance = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    