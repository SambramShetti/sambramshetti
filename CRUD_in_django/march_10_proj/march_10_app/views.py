from django.shortcuts import render, redirect
from .models import Product
from .form import ItemForm
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    product = Product.objects.all()

    item_nam = request.GET.get('item_nam')
    if item_nam != "" and item_nam != None:
        product = product.filter(item_name__icontains = item_nam)

    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    product = paginator.get_page(page)

    return render(request, "march_10_app/home.html", {'product':product})

def add_prod(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'march_10_app/add_prod.html', {'form':form})

def get_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'march_10_app/details.html', {'product':product})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'march_10_app/update_product.html', {'product':product, 'form':form})

# def delete_product(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('home')
#     return render(request, 'march_10_app/delete_product.html',{'product':product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'yes':
            product.delete()
            return redirect('home')
        elif action == 'no':
            return redirect('get_details', id=id)
    return render(request, 'march_10_app/delete_product.html',{'product':product})