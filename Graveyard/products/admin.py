from django.contrib import admin
from .models import Product
from .models import VPN
from .models import Giftcard


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "active", "created")
    list_filter = ("active",)
    search_fields = ("name",)
    ordering = ("-created",)


@admin.register(VPN)
class VPNAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "type", "duration", "limit", "renewable", "active", "created")
    list_filter = ("type", "renewable", "active")
    search_fields = ("name", "type")
    ordering = ("-created",)


@admin.register(Giftcard)
class GiftcardAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "type", "country", "active", "created")
    list_filter = ("type", "country", "active")
    search_fields = ("name", "type", "country")
    ordering = ("-created",)
