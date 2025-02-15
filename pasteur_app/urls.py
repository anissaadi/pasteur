from django.urls import path
from . import views

urlpatterns = [
  path('', views.CertificatCreateView.as_view(), name='soumettre_certificat'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('certificat/<int:certificat_id>/pdf_html/', views.generer_pdf_certificat_html, name='generer_pdf_certificat_html'),
]
