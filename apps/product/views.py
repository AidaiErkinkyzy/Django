from django.shortcuts import render

from django.views.generic import ListView
from .models import Food, Category

# Create your views here.


class ProductListView(ListView):
    model = Food
    template_name = 'pages/product_list.html'
    context_object_name = 'product_list'
    queryset = Food.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
