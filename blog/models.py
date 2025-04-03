from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    statut = models.CharField(max_length=20, choices=[
        ('brouillon', 'Brouillon'),
        ('publie', 'Publié')
    ], default='brouillon')
    
    # Informations sur l'étudiant
    nom_etudiant = models.CharField(max_length=100, default='')
    prenom_etudiant = models.CharField(max_length=100, default='')
    numero_etudiant = models.CharField(max_length=20, default='')
    filiere = models.CharField(max_length=100, default='')
    niveau = models.CharField(max_length=50, default='')
    email_etudiant = models.EmailField(default='')
    telephone = models.CharField(max_length=20, default='')
    date_naissance = models.DateField(null=True, blank=True)
    photo_etudiant = models.ImageField(upload_to='etudiants/', null=True, blank=True)

    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
