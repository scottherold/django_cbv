from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class CBView(View):
    """This is a class for a class based view example"""

    def get(self, request):
        """The function to process HTTP GET requests for the class.

        Parameters:
            request (HTTPRequest): The HTTP request to process.

        Returns:
            HttpResponse: A string sent to the client as a HTTP response.
        """
        return HttpResponse('CLASS BASED VIEWS ARE COOL')