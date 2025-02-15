from django.db import models
from django.utils.translation import gettext_lazy as _

class Certificat(models.Model):
    # --- Core Identification and Indexing ---
    denomination_commerciale = models.CharField(
        max_length=255,
        verbose_name=_("Dénomination commerciale"),
        db_index=True  # Index for faster searching and filtering
    )
    designation = models.CharField(
        max_length=255,
        verbose_name=_("Désignation"),
        db_index=True  # Index for faster searching and filtering
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        db_index=True  # Index for filtering by date ranges
    )
    est_valide = models.BooleanField(
        default=False,
        db_index=True,  # Index for filtering valid/invalid certificates
        verbose_name=_("Est Valide")  # Added verbose name for clarity
    )

    # --- Information about Pharmaceutical and Manufacturing Entities ---
    nom_pharma = models.CharField(
        max_length=200,
        verbose_name=_("Nom et prénom du pharmacien directeur technique")
    )
    nom = models.CharField(
        max_length=100,
        verbose_name=_("Nom de l'établissement de détenteur/titulaire de l'autorisation de commerciale provisoire (ACP)")
    )
    adress = models.CharField(
        verbose_name=_("Adresse de l'établissement de détenteur/titulaire de l'autorisation de commerciale provisoire (ACP)"),
        max_length=400
    )
    nom_produit = models.CharField(
        verbose_name=_("Nom de l'établissemnt exploitant de ACP"),
        max_length=400
    )
    adress_produit = models.CharField(
        verbose_name=_("Adresse de l'établissemnt exploitant de ACP"),
        max_length=400
    )
    nom_fabric = models.CharField(
        max_length=400,
        verbose_name=_("Nom de l'établissement fabriquant du dispositif médical")
    )
    adress_fabric = models.CharField(
        max_length=400,
        verbose_name=_("Adresse de site de fabrication du dispositif médical")
    )
    organisme = models.TextField(
        verbose_name=_("Organismes Certificateurs ou Organismes Equivalentes")
    )

    # --- Details from the Document ---
    classification = models.CharField(
        max_length=255,
        verbose_name=_("Classification")
    )
    caracteristiques = models.TextField(
        verbose_name=_("Caractéristiques")
    )
    conditions_conservation = models.TextField(
        verbose_name=_("Conditions de conservation")
    )
    duree_stabilite = models.CharField(
        max_length=100,
        verbose_name=_("Durée de stabilité")
    )

    # --- File Attachment ---
    fichier_pdf = models.FileField(
        upload_to='certificats_pdf/',
        verbose_name=_("Fichier PDF Joint"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Certificat")  # Translatable model name
        verbose_name_plural = _("Certificats")  # Translatable plural name
        indexes = [
        models.Index(fields=['denomination_commerciale', 'designation'], name='cert_name_desig_idx'), # <-- Shortened index name
    ]
        ordering = ['-date_creation', 'denomination_commerciale'] # Default ordering for lists

    def __str__(self):
        return f"Certificat {self.pk} - {self.denomination_commerciale}"