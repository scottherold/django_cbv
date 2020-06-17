from django.shortcuts import render
from django.views.generic import View,TemplateView


# Create your views here.
class IndexView(TemplateView):
    """This is a class that displays the basic_app/index/html file.

    Attributes:
        template_name (str): Path to template to be displayed by view.
    """
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        """
        Produces context for template.

        Returns:
            context: A dictionary of context key/value pairs that can be
            accessed by the index.html template.
        """
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context