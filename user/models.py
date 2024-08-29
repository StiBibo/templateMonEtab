from django.db import models

# Create your models here.

class User(models.Model):
    pseudo = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250,)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.pseudo} : {self.password}'
    
    # class Meta:
    #     verbose_name = 'Student'
    #     verbose_name_plural = 'Utilisateurs'
    

