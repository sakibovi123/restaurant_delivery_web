# Generated by Django 3.2.6 on 2022-01-03 14:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('brand_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('category_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_sign', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('shop_name', models.CharField(max_length=255, unique=True)),
                ('shop_address1', models.TextField(blank=True, null=True)),
                ('shop_address2', models.TextField(blank=True, null=True)),
                ('shop_contact', models.CharField(max_length=255, null=True)),
                ('shop_bin_no', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_vat', models.CharField(blank=True, max_length=255, null=True)),
                ('mushak_no', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_logo', models.ImageField(null=True, upload_to='images/')),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('vat_amount', models.FloatField(default=0, null=True)),
                ('show_mushak', models.BooleanField(default=False, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.currency')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('tax_id', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('trade_license', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.citymodel')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.countrymodel')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False, null=True)),
                ('can_config_pos', models.BooleanField(default=False, null=True)),
                ('can_config_roles', models.BooleanField(default=False, null=True)),
                ('can_config_orders', models.BooleanField(default=False, null=True)),
                ('can_config_inventory', models.BooleanField(default=False, null=True)),
                ('can_config_customers', models.BooleanField(default=False, null=True)),
                ('can_config_vendors', models.BooleanField(default=False, null=True)),
                ('can_config_tables', models.BooleanField(default=False, null=True)),
                ('can_config_emps', models.BooleanField(default=False, null=True)),
                ('can_manage_settings', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('buying_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock_amount', models.PositiveIntegerField(default=0)),
                ('out_of_stock', models.BooleanField(blank=True, default=False, null=True)),
                ('item_img', models.ImageField(null=True, upload_to='images/')),
                ('product_descriptions', models.TextField(null=True)),
                ('upc', models.IntegerField(blank=True, null=True)),
                ('sku', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.shop')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.vendor')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('emp_username', models.CharField(max_length=255, unique=True)),
                ('emp_pin', models.CharField(max_length=255)),
                ('confirm_pin', models.CharField(max_length=255, null=True)),
                ('emp_profile_pic', models.ImageField(upload_to='images/')),
                ('is_active', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('BANN', 'BANN')], max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.roles')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='citymodel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.countrymodel'),
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_received', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('change', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], max_length=255, null=True)),
                ('payment_method', models.CharField(choices=[('CASH', 'CASH'), ('Credit Card', 'Credit Card'), ('bKash', 'bKash'), ('Nagad', 'Nagad')], default='CASH', max_length=120, null=True)),
                ('payment_number', models.CharField(blank=True, max_length=120, null=True)),
                ('items', models.ManyToManyField(to='app.CartItems')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.shop')),
                ('sold_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.employee')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.shop'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
        migrations.AddField(
            model_name='brand',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.shop'),
        ),
    ]
