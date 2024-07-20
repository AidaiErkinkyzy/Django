from django.shortcuts import render
from .forms import ContactUsForm
# Create your views here.
from django.views.generic import FormView, CreateView





class ContactUsView(CreateView):
    form_class = ContactUsForm
    template_name = "pages/contact_us.html"
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)