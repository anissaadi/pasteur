# forms.py
from django import forms
from .models import Certificat

class CertificatForm(forms.ModelForm):
    class Meta:
        model = Certificat
        fields = [
            'nom_pharma',
            'nom',
            'adress',
            'nom_produit',
            'adress_produit',
            'nom_fabric',
            'adress_fabric',
            'organisme',
            'denomination_commerciale',
            'designation',
            'classification',
            'caracteristiques',
            'conditions_conservation',
            'duree_stabilite',
            'fichier_pdf',
        ]
