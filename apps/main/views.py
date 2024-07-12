from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import *

class IndexView(TemplateView):
    template_name = "pages/index_home.html"


class AboutUsView(TemplateView):
    template_name = "page/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_us"] = AboutUs.object.first()
        context["employees"] = Employees.object.all()
        return context
