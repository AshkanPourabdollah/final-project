from django.shortcuts import render, HttpResponse

from products.models import Product


# Create your views here.
def home_view(request):
    products = Product.objects.all()[2:10]
    return render(request, 'pages/home_page.html', context={'products': products})

def contact_view(request):
    return render(request, 'pages/contact_page.html')

def about_view(request):
    return render(request, 'pages/about_page.html')
