from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register([
    Currency,
    Shop,
    CountryModel,
    CityModel,
    Vendor,
    Roles,
    Employee,
    Category,
    Brand,
    Item,
    CartItems,
    Checkout,
    ItemType
])