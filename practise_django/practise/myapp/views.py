from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    product = Product.objects.all()

    # Search bar codes
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name != None:
        product = product.filter(title__icontains = item_name)

    # pagination codes
    paginator = Paginator(product, 2)
    page = request.GET.get('page')
    product = paginator.get_page(page)

    return render(request, 'myapp/home.html',{'product':product})


def details(request, id):
    product_obj = Product.objects.get(id=id)

    return render(request, 'myapp/details.html',{"product_obj":product_obj})

