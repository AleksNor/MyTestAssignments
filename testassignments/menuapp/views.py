from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'menuapp/index.html'