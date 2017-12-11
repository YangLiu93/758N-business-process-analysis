from django.contrib import admin
from .models import Orders, Product, ProductOrder, return_order

# Register your models here.
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(return_order)