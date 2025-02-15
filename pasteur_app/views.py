# views.py
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from .models import Certificat
from .forms import CertificatForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.shortcuts import get_object_or_404
from .models import Certificat


def generer_pdf_certificat_html(request, certificat_id):

    certificat = get_object_or_404(Certificat, pk=certificat_id)

    context = {'certificat': certificat}
    

    html_string = render_to_string('certificat_pdf.html', context)
    

    base_url = request.build_absolute_uri('/')
    
 
    html = HTML(string=html_string, base_url=base_url)
    
    
    css = CSS(string='@page { size: A4; margin: 1cm }')
    
    pdf = html.write_pdf(stylesheets=[css])
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificat_{}.pdf"'.format(certificat_id)
    return response




def link_callback(uri, rel):
 
    import os
    from django.conf import settings


    sUrl = settings.STATIC_URL        
    sRoot = settings.STATIC_ROOT      
    mUrl = settings.MEDIA_URL         
    mRoot = settings.MEDIA_ROOT       

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


class CertificatCreateView(CreateView):
    model = Certificat
    form_class = CertificatForm
    template_name = 'soumettre_certificat.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        messages.success(self.request, "Votre demande a été soumise avec succès !")
        self.object = form.save() 
        return redirect(reverse_lazy('success') + f'?certificat_id={self.object.pk}')

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur est survenue. Veuillez vérifier vos informations.")
        return super().form_invalid(form)

class SuccessView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certificat_id'] = self.request.GET.get('certificat_id') # Récupère l'ID de l'URL
        return context

