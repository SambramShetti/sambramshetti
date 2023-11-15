from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "E-commerce Site" # to change admin page header
admin.site.site_title = "E-commerce" # to change admin site title(in url)
admin.site.index_title = "Manage E-commerce site" # to change admin index title



# below codes helps to display mentioned field  instead of just displaying title of product
class ProductAdmin(admin.ModelAdmin):
    def change_category(self, request, queryset):
        '''
        This function is used to have dropdown that will make category(or any field) set to default in "actions" dropdown.
        '''
        queryset.update(category="default")

    change_category.short_description = "Default Category" # if u want to change dropdown name, change here. i.e change "Default Category" to any name
    
    list_display = ('title', 'price', 'discount_price', 'category') # this will list only these mentioned fields in list page.
    search_fields = ('title','category') # This will give search bar to search for title and caegory in list page.
    actions = ('change_category',) # refer change_category function.
    fields = ('title', 'price', 'category') # this line will display these mentioned fields in productss page instead of entire fields.
    list_editable = ('price', 'category') # this will enable admins to edit mentioned columns in list page.


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)