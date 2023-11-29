from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ("name", "amount", "category") # specify the field names which u want user to fill in the form.
