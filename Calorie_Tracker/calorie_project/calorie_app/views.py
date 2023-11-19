from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def home(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed'] # this will fetch only food name when user hits add button and not food object.
        consume = Food.objects.get(name = food_consumed) # this will get food object which user has select in above line of code.
        user = request.user # this will get which user is logged in currently and adds food item to that user.
        consume = Consume(user=user, food_consumed=consume) # this is object for class Consume. this will add/tell us which user added/consumed which food and stores it in Consume db.
        consume.save()
        foods = Food.objects.all() # this will show all available items to user 
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user) # This will give all food items consumed by current user
    return render(request, 'calorie/home.html', {"foods":foods, "consumed_food":consumed_food})

def delete_item(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    return render(request, 'calorie/delete.html')