from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != "" and item_name != None:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4) # gives 4 products in 1 page
    page = request.GET.get('page') # gives current page no
    product_objects = paginator.get_page(page) # this will fetch all objects(products) in current page and not all objects

    return render(request, 'shop/home.html', {'product_objects':product_objects})

def details(request, id):
    product_object = Products.objects.get(id = id)

    return render(request, 'shop/details.html', {'product_object':product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        total = request.POST.get('total',"")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
        order.save()
    return render(request, 'shop/checkout.html')