from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class IndexView(View):
    def get(self, request):
        products = Product.objects.all()[:3]

        context = {
            "products" : products
        }
        return render(request, "index.html", context)