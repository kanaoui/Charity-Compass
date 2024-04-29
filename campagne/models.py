from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campagne(models.Model):
    charity_number = models.CharField(max_length=50)
    slug = models.SlugField()
    nom = models.CharField(max_length=100)
    histoire = models.TextField()
    montant = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    supporteurs = models.IntegerField(max_length=100, null = True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    fundraiser = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nom
    
    def snippet(self):
        return self.histoire[:50] + '...'