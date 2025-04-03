from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'titre', 'contenu', 'image', 'statut',
            'nom_etudiant', 'prenom_etudiant', 'numero_etudiant',
            'filiere', 'niveau', 'email_etudiant', 'telephone',
            'date_naissance', 'photo_etudiant'
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'contenu': forms.Textarea(attrs={'rows': 10}),
        } 