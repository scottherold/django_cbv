from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
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
        context_object_name (str): names the context object 'schools' instead
        of the default school_list provided by the ListView class.
    """
    model = models.School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    """This is a class that displays the details of a particular school to the
    school_detail.html template

    Attributes:
        model (Model): The school database model (table). Creates a link to the
        database for querying.
        template_name (str): The location for school_detail.html in the file
        structure.
        context_object_name (str): names the context object 'school_detail'
        instead of the default school provided by the DetailView class.
    """
    model = models.School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'


class SchoolCreateView(CreateView):
    """This is a class that creates a new School with data provided from the
    client.

    Attributes:
        fields (tuple(str)): The list of fields expected to be mapped from the
        client to the School model during creation.
        model (Model): The school database model (table). Creates a link to the
        database for creation.
    """
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    """This is a class that updates an existing School with data provided from
    the client.

    Attributes:
        fields (tuple(str)): The list of fields expected to be mapped from the
        client to the School model for updating.
        model (Model): The school database model (table). Creates a link to the
        database for updating.
    """
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    """This is a class that deletes an existing School with the PK provided
    from the client.

    Attributes:
        model (Model): The school database model (table). Creates a link to the
        database for deleting.
        success_url (function): Uses the django urls reverse_lazy() function to
        route the request to the basic_app:list url once the data has been
        successfully delete.
    """
    model = models.School
    success_url = reverse_lazy("basic_app:list")