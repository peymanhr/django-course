from django.contrib import admin
from django.utils.html import format_html
from .models import Product
from .models import VPN
from .models import Giftcard


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "product_type", "properties", "active", "created")
    list_filter = ("active",)
    search_fields = ("name",)
    ordering = ("-created",)

    def get_queryset(self, request):
        return super().get_queryset(request)

    def product_type(self, obj):
        if hasattr(obj, "vpn"):
            return "VPN"
        elif hasattr(obj, "giftcard"):
            return "Giftcard"
        return None

    def properties(self, obj):
        if hasattr(obj, "vpn"):
            return format_html(
                f"VPN Type: {obj.vpn.type} <br> Duration: {obj.vpn.duration} days <br> Limit: {obj.vpn.limit} GiB"
            )
        elif hasattr(obj, "giftcard"):
            return format_html(
                f"Giftcard Type: {obj.giftcard.type} <br> Country: {obj.giftcard.country}"
            )
        return "-"

    product_type.short_description = "Type"
    properties.short_description = "Details"


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
