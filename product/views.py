from django.shortcuts import render
from product.models import Product


# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        context = {
            'products': product
        }

        return render(request, 'products/product.html', context=context)
