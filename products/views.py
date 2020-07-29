from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ A view to return products page, sorting and search """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)