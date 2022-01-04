from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from PIL import Image


class ItemType(models.Model):
    type_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.type_name


class Currency(models.Model):
    currency_sign = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.currency_sign


class Shop(models.Model):
    created_at = models.DateField(default=date.today)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, unique=True)
    shop_address1 = models.TextField(null=True, blank=True)
    shop_address2 = models.TextField(null=True, blank=True)
    shop_contact = models.CharField(max_length=255, null=True)
    shop_bin_no = models.CharField(max_length=255, null=True, blank=True)
    shop_vat = models.CharField(max_length=255, null=True, blank=True)
    mushak_no = models.CharField(max_length=255, null=True, blank=True)
    shop_logo = models.ImageField(upload_to="images/", null=True)
    is_active = models.BooleanField(default=False, null=True)
    vat_amount = models.FloatField(null=True, default=0)
    show_mushak = models.BooleanField(default=False, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.shop_name


class CountryModel(models.Model):
    country_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.country_name


class CityModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.city_name


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    tax_id = models.IntegerField(null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    address = models.TextField(null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True)
    zip_code = models.IntegerField(null=True, blank=True)
    trade_license = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True)
    contact_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.vendor_name


class Roles(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, null=True)
    role_title = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False, null=True)
    can_config_pos = models.BooleanField(default=False, null=True)
    can_config_roles = models.BooleanField(default=False, null=True)
    can_config_orders = models.BooleanField(default=False, null=True)
    can_config_inventory = models.BooleanField(default=False, null=True)
    can_config_customers = models.BooleanField(default=False, null=True)
    can_config_vendors = models.BooleanField(default=False, null=True)
    can_config_tables = models.BooleanField(default=False, null=True)
    can_config_emps = models.BooleanField(default=False, null=True)
    can_manage_settings = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(default=datetime.now, null=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.id)



class Employee(models.Model):
    STATUS_CHOICE = (
        ("ACTIVE", "ACTIVE"),
        ("BANN", "BANN")
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=255)
    emp_username = models.CharField(max_length=255, unique=True)
    emp_pin = models.CharField(max_length=255)
    confirm_pin = models.CharField(max_length=255, null=True)
    emp_profile_pic = models.ImageField(upload_to="images/")
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    is_active = models.CharField(max_length=255, null=True, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.emp_username


class Category(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    brand_name = models.CharField(max_length=255)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.brand_name


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    buying_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    stock_amount = models.PositiveIntegerField(default=0)
    out_of_stock = models.BooleanField(default=False, null=True, blank=True)
    item_img = models.ImageField(upload_to="images/", null=True)
    product_descriptions = models.TextField(null=True)
    upc = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

        if not self.item_img:
            return

        imag = Image.open(self.item_img.path)
        if imag.width > 400 or imag.height > 400:
            output_size = (400, 400)
            imag.thumbnail(output_size)
            imag.save(self.item_img.path)

    @property
    def get_items_by_category(self):
        return Item.objects.filter(category__item_name=self.title)

    @staticmethod
    def get_items(ids):
        return Item.objects.filter(id__in=ids)



class CartItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class Checkout(models.Model):
    STATUS_CHOICE = (
        ("PAID", "PAID"),
        ("UNPAID", "UNPAID")
    )
    PAYMENT_CHOICE = (
        ("CASH", "CASH"),
        ("Credit Card", "Credit Card"),
        ("bKash", "bKash"),
        ("Nagad", "Nagad")
    )

    sold_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(CartItems)
    discount = models.IntegerField(null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    grand_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    amount_received = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    change = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, null=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS_CHOICE)
    payment_method = models.CharField(max_length=120, null=True, choices=PAYMENT_CHOICE, default="CASH")
    payment_number = models.CharField(max_length=120, null=True, blank=True)
    

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.id)
