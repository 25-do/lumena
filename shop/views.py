from django.shortcuts import render
from django.views import View
from .models import Product, Category
# Create your views here.
class IndexView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related("products").all()
        category_data = {}

        for category in categories:
            category_data[category] = category.products.all()  # Fetch products per category

        return render(request, "index.html", {"categories": category_data})