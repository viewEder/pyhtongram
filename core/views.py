from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    # Atributos de la clase:
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)