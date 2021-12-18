from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    # Atributos de la clase:
    template_name = "core/index.html"
    diccionario_contexto = {
        'titulo': '¡Únete a Nuestra Red!',
        'parrafo': 'PytonGRAM is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.',
        'boton': 'Unirme a la red'
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.diccionario_contexto)