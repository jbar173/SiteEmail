from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SuccessView(TemplateView):
    template_name = 'enquiry/success.html'
