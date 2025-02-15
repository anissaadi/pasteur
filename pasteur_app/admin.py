# admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Certificat

@admin.register(Certificat)
class CertificatAdmin(admin.ModelAdmin):
    list_display = (
        'denomination_commerciale',
        'est_valide',
        'date_creation',
        'pdf_download_button',
        'fichier_joint_button',
        'fichier_pdf_filename'
    )
    actions = ['valider_certificats']
    fields = (
        'nom_pharma', 'nom', 'adress', 'nom_produit', 'adress_produit',
        'nom_fabric', 'adress_fabric', 'organisme',
        'denomination_commerciale', 'designation', 'classification', 'caracteristiques',
        'conditions_conservation', 'duree_stabilite', 'est_valide', 'fichier_pdf'
    )
    change_form_template = 'admin/pasteur_app/change_form.html'
    # Uncomment and configure search_fields to enable search:
    search_fields = ('denomination_commerciale', 'designation', 'nom_pharma', 'nom') # Add fields you want to search on

    def valider_certificats(self, request, queryset):
        queryset.update(est_valide=True)
        self.message_user(request, "Le(s) certificat(s) sélectionné(s) ont été validés.")
    valider_certificats.short_description = "Valider les certificats sélectionnés"

    def fichier_pdf_filename(self, obj):
        if obj.fichier_pdf:
            return obj.fichier_pdf.name.split('/')[-1]
        return "-"
    fichier_pdf_filename.short_description = "Fichier PDF"

    def pdf_download_button(self, obj):
        """
        Crée un bouton HTML pour télécharger le PDF du certificat généré.
        """
        url = reverse('generer_pdf_certificat_html', args=[obj.pk])
        return format_html('<a class="button" href="{}" target="_blank">Imprimer PDF</a>', url)
    pdf_download_button.short_description = 'Imprimer PDF Généré'

    def fichier_joint_button(self, obj):
        """
        Crée un bouton HTML pour imprimer le fichier PDF joint (si existant).
        """
        if obj.fichier_pdf:
            return format_html('<a class="button" href="{}" target="_blank">Imprimer Fichier Joint</a>', obj.fichier_pdf.url)
        return "-"
    fichier_joint_button.short_description = 'Imprimer Fichier Joint'
    fichier_joint_button.allow_tags = True

    def has_delete_permission(self, request, obj=None):
        """
        Désactive la permission de suppression pour le modèle Certificat.
        """
        return False