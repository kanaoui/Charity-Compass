from django.db import models

# Create your models here.
class Campagne(models.Model):
    charity_number = models.CharField(max_length=50)
    slug = models.SlugField()
    nom = models.CharField(max_length=100)
    histoire = models.TextField()
    montant = models.DecimalField(max_digits=6, decimal_places=2)
    supporteurs = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
    def snippet(self):
        return self.histoire[:50] + '...'