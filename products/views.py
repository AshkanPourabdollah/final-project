from django.shortcuts import render

from products.models import Product
import random


# Create your views here.
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list_page.html', context={"products": products})


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    random_products = random.sample(list(Product.objects.all()), 4)
    return render(request, 'products/product_detail_page.html', context={"product": product, "random_products": random_products})
