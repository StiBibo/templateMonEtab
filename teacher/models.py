from django.db import models

# Create your models here.

matiere = {
    ("MATH", "MATHEMATIQUE"),
   ("PHY", "PHYSIQUE"),
   ("SVT", "SVT")
}

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sexe = models.BooleanField(default=False)
    date_de_naissance = models.CharField(max_length=255)
    matiere = models.CharField(max_length=25,choices=matiere)
    numero_de_telephone = models.CharField(max_length=15)
    ville = models.CharField(max_length=15)
    vacant = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} : matiere de {self.matiere}'
