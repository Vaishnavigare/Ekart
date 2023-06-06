from django.contrib import admin
from ecomapp.models import Product,Order,Orderhistory
# Register your models here.

#admin.site.register(Product)

#Define ModelAdminClass

class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status','pimage','pdes']
    list_filter=['status','cat']



admin.site.register(Product,ProductAdminClass)
admin.site.register(Order)
admin.site.register(Orderhistory)

admin.site.site_header="Ekart Dashboard"

