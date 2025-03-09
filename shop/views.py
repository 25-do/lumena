from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class IndexView(View):
    def get(self, request):
        all_products = list(Product.objects.all())  # Fetch once & convert to list

        products = all_products[:10]
        products1 = all_products[10:20]
        products2 = all_products[20:30]
        context = {
            "products" : products,
            "products1" : products1,
            "products2" : products2
        }
        return render(request, "index.html", context)