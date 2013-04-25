from django.db import models

class Tipo(models.Model):
    tipo_choice = (
        ('C', 'Colegio'),
        ('M', 'Mixta'),
        
    )

    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length=2, choices=tipo_choice)      
