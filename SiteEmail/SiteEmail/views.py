from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from enquiry.models import Enquiry,EnquiryEmail
from . import forms
from s_email import forward_enquiry

class CreateEnquiry(CreateView):
    model = Enquiry
    template_name = 'enquiry.html'
    form_class = forms.CreateEnquiryForm
    success_url = reverse_lazy('enquiry:success')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        x = EnquiryEmail.objects.create(enquiry=self.object)
        x.save()
        forward_enquiry(x)
        return super().form_valid(form)
