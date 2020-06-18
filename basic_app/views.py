from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models


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


class SchoolListView(ListView):
    """This is a class that provides a list of every school in the database.

    Attributes:
        model (Model): The school database model (table). Creates a link to the
        database for querying.
    """
    model = models.School


class SchoolDetailView(DetailView):
    """This is a class that displays the details of a particular school to the
    school_detail.html template

    Attributes:
        model (Model): The school database model (table). Creates a link to the
        database for querying.
        template_name (str): The location for school_detail.html in the file
        structure.
    """
    model = models.School
    template_name = 'basic_app/school_detail.html'