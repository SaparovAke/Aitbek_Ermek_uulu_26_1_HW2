from django.shortcuts import render, redirect
from product.models import Product, Review
from product.forms import ProductCreateForm, CommentCreateForm
from product.constants import PAGINATION_LIMIT


# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search:
            product = product.filter(product_name__icontains=search) | product.filter(description__icontains=search)
        max_page = product.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)
        product = product[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]
        context = {
            'products': product,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }

        return render(request, 'products/product.html', context=context)

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': CommentCreateForm,
            'user': request.user
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=id
            )
        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': form
        }

        return render(request, 'products/create.html', context=context)
def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                product_name=form.cleaned_data.get('product_name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                image=form.cleaned_data.get('image')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
