from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class IndexView(View):
    def get(self, request):
        products = Product.objects.all()[:10]
        products1 = Product.objects.all()[10:20]
        products2 = Product.objects.all()[20:30]

        context = {
            "products" : products,
            "products1" : products1,
            "products2" : products2
        }
        return render(request, "index.html", context)