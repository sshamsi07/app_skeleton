from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'build/index.html'