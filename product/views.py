from django.shortcuts import render
from product.models import Product, Review


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

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)