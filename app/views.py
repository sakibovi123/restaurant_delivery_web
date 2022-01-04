from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.views import View
# Create your views here.


class PanelHomeView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render(request, "panel/home.html", args)
        else:
            return redirect("warning")


class GETVendorView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("")
    
    """Delete Vendor"""

    def post(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if vendorId.id != None:
            vendorId.delete()
            return redirect(f"")


class AddVendorView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("")
    
    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                vendor_name = request.POST.get("vendor_name")
                tax_id = request.POST.get("tax_id")
                shop = shopId.id
                address = request.POST.get("address")
                country = request.POST.get("country")
                city = request.POST.get("City")
                zip_code = request.POST.get("zip_code")
                trade_license = request.POST.get("trade_license")
                phone_number = request.POST.get("phone_number")
                contact_name = request.POST.get("contact_number")
                email = request.POST.get("email")
                website = request.POST.get("website")

                """
                mendatory fields: vendor_name, address, country, city, phone_number, email
                """

                if tax_id != "" and zip_code != "" and trade_license != "" and website != "":
                    Vendor.objects.create(
                        vendor_name=vendor_name,
                        tax_id=tax_id,
                        shop=shop,
                        address=address,
                        country=CountryModel.objects.get(id=country),
                        city=CityModel.objects.get(id=city),
                        zip_code=zip_code,
                        trade_license=trade_license,
                        phone_number=phone_number,
                        contact_name=contact_name,
                        email=email,
                        website=website

                    ) 
                    return redirect(f"")
                else:
                    Vendor.objects.create(
                        vendor_name=vendor_name,
                        shop=shop,
                        address=address,
                        country=CountryModel.objects.get(id=country),
                        city=CityModel.objects.get(id=city),
                        phone_number=phone_number,
                        email=email,
                    )

                    return redirect(f"")


class UpdateVendorView(View):
    def get(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("warning")

    def post(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if request.method == "POST":
            if vendorId.tax_id == "" and vendorId.zip_code == "" and vendorId.trade_license == "" and vendorId.website == "":
                vendorId.vendor_name = request.POST.get("vendor_name")
                vendorId.shop = shopId.id
                vendorId.address = request.POST.get("address")
                vendorId.country = request.POST.get("country")
                vendorId.city = request.POST.get("city")
                vendorId.phone_number = request.POST.get("phone_number")
                vendorId.email = request.POST.get("email")

                vendorId.save()

                return redirect("")
            else:
                vendorId.vendor_name = request.POST.get("vendor_name")
                vendorId.tax_id = request.POST.get("tax_id")
                vendorId.shop = shopId.id
                vendorId.address = request.POST.get("address")
                vendorId.country = request.POST.get("country")
                vendorId.city = request.POST.get("City")
                vendorId.zip_code = request.POST.get("zip_code")
                vendorId.trade_license = request.POST.get("trade_license")
                vendorId.phone_number = request.POST.get("phone_number")
                vendorId.contact_name = request.POST.get("contact_number")
                vendorId.email = request.POST.get("email")
                vendorId.website = request.POST.get("website")

                vendorId.save()
                return redirect(f"")


class GETROlesView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)

        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect(f"")

    """Deleting Roles"""
    def post(self, request, shop_id, role_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        roleId = get_object_or_404(Roles, pk=role_id)
        if request.method == "POST":
            roleId.delete()

            return redirect()


class AddRolesView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("")
    
    
    def post(self, request, shop_id):
        if request.method == "POST":
            role_title = request.POST.get("role_title")
            shop = Shop.objects.get(id=shop_id.id)
            is_admin = request.POST.get("is_admin")
            can_config_pos = request.POST.get("can_config_pos")
            can_config_roles = request.POST.get("can_config_roles")
            can_config_orders = request.POST.get("can_config_orders")
            can_config_inventory = request.POST.get("can_config_inventory")
            can_config_customers = request.POST.get("can_config_customers")
            can_config_vendors = request.POST.get("can_config_vendors")
            can_config_tables = request.POST.get("can_config_tables")
            can_config_emps = request.POST.get("can_config_emps")
            can_manage_settings = request.POST.get("can_manage_settings")

            if is_admin == "yes":
                is_admin = True
            else:
                is_admin = False
            if can_config_pos == "yes":
                can_config_pos = True
            else:
                can_config_pos = False
            if can_config_roles == "yes":
                can_config_roles = True
            else:
                can_config_roles = False
            if can_config_orders == "yes":
                can_config_orders = True
            else:
                can_config_orders = False
            if can_config_inventory == "yes":
                can_config_inventory = True
            else:
                can_config_inventory = False
            if can_config_customers == "yes":
                can_config_customers = True
            else:
                can_config_customers = False
            if can_config_vendors == "yes":
                can_config_vendors = True
            else:
                can_config_vendors = False
            if can_config_tables == "yes":
                can_config_tables = True
            else:
                can_config_tables = False
            if can_config_emps == "yes":
                can_config_emps = True
            else:
                can_config_emps = False
            if can_manage_settings == "yes":
                can_manage_settings = True
            else:
                can_manage_settings = False

            # Saving
            rl = Roles(
                role_title=role_title,
                shop=shop,
                is_admin=is_admin,
                can_config_pos=can_config_pos,
                can_config_roles=can_config_roles,
                can_config_orders=can_config_orders,
                can_config_inventory=can_config_inventory,
                can_config_customers=can_config_customers,
                can_config_vendors=can_config_vendors,
                can_config_tables=can_config_tables,
                can_config_emps=can_config_emps,
                can_manage_settings=can_manage_settings
            )
            rl.save()
            # tRash model
            # trl = RolesTrashModel(
            #     role=rl,
            #     role_title=role_title,
            #     shop=shop,
            #     is_admin=is_admin,
            #     can_config_pos=can_config_pos,
            #     can_config_roles=can_config_roles,
            #     can_config_orders=can_config_orders,
            #     can_config_inventory=can_config_inventory,
            #     can_config_customers=can_config_customers,
            #     can_config_vendors=can_config_vendors,
            #     can_config_tables=can_config_tables,
            #     can_config_emps=can_config_emps,
            #     can_manage_settings=can_manage_settings
            # )
            # trl.save()

            return redirect(f"")


class UpdateRolesView(View):
    def get(self, request, shop_id, role_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        roleId = get_object_or_404(Roles, pk=role_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("")
    

    def post(self, request, shop_id, role_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        roleId = get_object_or_404(Roles, pk=role_id)
        if shopId.user == request.user and request.method == "POST":
            roleId.shop = Shop.objects.get(id=shop_id.id)
            role_title = request.POST.get("role_title")
            is_admin = request.POST.get("is_admin")
            can_config_pos = request.POST.get("can_config_pos")
            can_config_roles = request.POST.get("can_config_roles")
            can_config_orders = request.POST.get("can_config_orders")
            can_config_inventory = request.POST.get("can_config_inventory")
            can_config_customers = request.POST.get("can_config_customers")
            can_config_vendors = request.POST.get("can_config_vendors")
            can_config_tables = request.POST.get("can_config_tables")
            can_config_emps = request.POST.get("can_config_emps")
            can_manage_settings = request.POST.get("can_manage_settings")

            if is_admin == "yes":
                is_admin = True
            else:
                is_admin = False
            if can_config_pos == "yes":
                can_config_pos = True
            else:
                can_config_pos = False
            if can_config_roles == "yes":
                can_config_roles = True
            else:
                can_config_roles = False
            if can_config_orders == "yes":
                can_config_orders = True
            else:
                can_config_orders = False
            if can_config_inventory == "yes":
                can_config_inventory = True
            else:
                can_config_inventory = False
            if can_config_customers == "yes":
                can_config_customers = True
            else:
                can_config_customers = False
            if can_config_vendors == "yes":
                can_config_vendors = True
            else:
                can_config_vendors = False
            if can_config_tables == "yes":
                can_config_tables = True
            else:
                can_config_tables = False
            if can_config_emps == "yes":
                can_config_emps = True
            else:
                can_config_emps = False
            if can_manage_settings == "yes":
                can_manage_settings = True
            else:
                can_manage_settings = False

            # Updating
            roleId.role_title = role_title
            roleId.is_admin = is_admin
            roleId.can_config_pos = can_config_pos
            roleId.can_config_roles = can_config_roles
            roleId.can_config_orders = can_config_orders
            roleId.can_config_inventory = can_config_inventory
            roleId.can_config_customers = can_config_customers
            roleId.can_config_vendors = can_config_vendors
            roleId.can_config_tables = can_config_tables
            roleId.can_config_emps = can_config_emps
            roleId.can_manage_settings = can_manage_settings

            roleId.save()
            
            # Updating Trash
            # trashRoleObj.role_title = role_title
            # trashRoleObj.is_admin = is_admin
            # trashRoleObj.can_config_pos = can_config_pos
            # trashRoleObj.can_config_roles = can_config_roles
            # trashRoleObj.can_config_orders = can_config_orders
            # trashRoleObj.can_config_inventory = can_config_inventory
            # trashRoleObj.can_config_customers = can_config_customers
            # trashRoleObj.can_config_vendors = can_config_vendors
            # trashRoleObj.can_config_tables = can_config_tables
            # trashRoleObj.can_config_emps = can_config_emps
            # trashRoleObj.can_manage_settings = can_manage_settings

            # trashRoleObj.save()

            return redirect(f"")


class GETEmployeeViw(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect(f"")
    
    """deleting and emp"""

    def post(self, request, shop_id, emp_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        empId = get_object_or_404(Employee, pk=emp_id)
        if shopId.user == request.user and request.method == "POST":
            empId.delete()

            return redirect(f"")
        else:
            return redirect("warning")


class AddEmployeeView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render(request, "", args)
        else:
            return redirect(f"")
    
    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user and request.method == "POST":
            shop = shopId.id
            full_name = request.POST.get("full_name")
            emp_username = request.POST.get("emp_username")
            emp_pin = request.POST.get("emp_pin")
            confirm_pin = request.POST.get("confirm_pin")
            emp_profile_pic = request.FILES.get("emp_profile_pic")
            role = request.POST.get("role")
            is_active = request.POST.get("is_active")
            emp = Employee(
                shop=shop,
                full_name=full_name,
                emp_username=emp_username,
                emp_pin=emp_pin,
                confirm_pin=confirm_pin,
                emp_profile_pic=emp_profile_pic,
                role=Roles.objects.get(id=role),
                is_active=True
            )
            emp.save()

            return redirect(f"")


class UpdateEmployeeView(View):
    def get(self, request, shop_id, emp_id):
        pass

    def post(self, request, shop_id, emp_id):
        pass


class GETCategoryView(View):
    def get():
        pass
    def post(self, request, shop_id, cat_id):
        pass


class AddCategoryView(View):
    def get(self, request, shop_id):
        pass

    def post(self, request, shop_id):
        pass

class UpdateCategoryView(View):
    def get(self, request, shop_id, cat_id):
        pass

    def post(self, request, shop_id, cat_id):
        pass

class GETBrandView(View):
    def get(self, request, shop_id):
        pass

    def post(self, request, shop_id, brand_id):
        pass


class AddBrandView(View):
    def get(self, request, shop_id):
        pass

    def post(self, request, shop_id):
        pass

class UpdateBrandView(View):
    def get(self, request, shop_id, brand_id):
        pass

    def post(self, request, shop_id, brand_id):
        pass


class GETItemView(View):
    def get(self, request, shop_id):
        pass

    def post(self, request, shop_id, item_id):
        pass


class AddItemView(View):
    def get(self, request, shop_id):
        pass

    def post(self, request, shop_id):
        pass

class UpdateItemView(View):
    def get(self, request, shop_id, item_id):
        pass

    def post(self, request, shop_id, item_id):
        pass