from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def allProductCat(request, cat_slug=None):
    cat_page = None
    products_list = None
    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        products_list = Product.objects.all().filter(category=cat_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': cat_page, 'products': products})

def proDetail(request, cat_slug, pro_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=pro_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
