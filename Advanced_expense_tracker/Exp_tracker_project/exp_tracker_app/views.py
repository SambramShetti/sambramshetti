'''
we are using tailwind for this project and for this reason, we need nodejs in our machine because we need npm(node package manager) for tailwind.
1. install node js in system
2. npm init -y # this will create package.json inside app directory
3. npm install tailwindcss@2.2.16 # tailwind package will be added in package.json file as dependency
4. create src.css file inside static folder.
5. add below code in package.json file
"build": "tailwind build exp_tracker_app/static/tracker_app/src.css -o exp_tracker_app/static/tracker_app/styles.css"
6. in terminal run following command
npm run build # this will create new styles.css file with all styling codes.
'''

from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime

# Create your views here.

def home(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount')) # to find total expense infrontend page instead of using javascript
    # print(total_expenses)

    # Logic to calculate last 365 days expense
    last_year = datetime.date.today() - datetime.timedelta(days=365) # substracting current datetime - datetime of 365 days before
    data = Expense.objects.filter(date__gt=last_year) # date__gt is nothing but date greater than last_year.
    yearly_sum = data.aggregate(Sum('amount')) # this will give yearly sum of expense.
    # print("yearly_sum: ", yearly_sum)

    # Logic to calculate last 30 days expense
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))

    # Logic to calculate last weekly expense
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    # Logic to calculate daily expense based on date
    daily_sums = Expense.objects.filter().values("date").order_by("date").annotate(sum=Sum('amount')) # this will filter on basis of date and order on basis of date
    # print("daily_sums: ", daily_sums)

    # Logic to calculate daily expense based on category
    categorical_sums = Expense.objects.filter().values("category").order_by("category").annotate(sum=Sum('amount')) # this will filter on basis of date and order on basis of date
    
    expense_form = ExpenseForm()
    return render(request, 'myapp/home.html', {"expense_form":expense_form, "expenses":expenses, "total_expenses":total_expenses, "yearly_sum":yearly_sum, "monthly_sum":monthly_sum, "weekly_sum":weekly_sum, "daily_sums":daily_sums, "categorical_sums":categorical_sums})

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense) # this will fetch form data in edit page
        if form.is_valid():
            form.save()
            return redirect("myapp:home")

    return render(request, "myapp/edit.html", {"expense_form":expense_form})



def delete(request, id):
    # expense = Expense.objects.get(id=id)
    # if request.method == "POST":
    #     expense.delete()
    #     return redirect("myapp:home")
    # return render(request, 'myapp/delete.html', {'expense':expense})

    # below code avoids delete.html and deletes that item once delete button is hit.

    if request.method == "POST" and 'delete' in request.POST: # this is because we have 2 post methods in home.html. so to avoid bugs, we added name=delete in delete button in home.html
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect("myapp:home")

    

