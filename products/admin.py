# Register your models here.

from django.contrib import admin

from .models import Product, Offer

#  from .models import Offer


# admin is the module. ModelAdmin is a class
# ModelAdmin class provides functionalities for managing models in the admin area
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    #  list_display is a PRE-BUILT attribute in the ModelAdmin class


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


#  ProductAdmin, OfferAdmin or any such model admin customization class.. inherits from the "ModelAdmin" class
#  To customize our Model Class(Product) in the admin area .. we need to create the class ProductAdmin
#  The naming system is by convention


admin.site.register(Product, ProductAdmin)
#  Here, we are telling Django, using the register(),
#  that we want Product to be managed in the "admin" area


admin.site.register(Offer, OfferAdmin)

