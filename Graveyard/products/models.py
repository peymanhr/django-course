from django.db import models
from django.utils.timezone import now
from .enums import VPNType, GiftcardType, Country


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimestampModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, db_index=True)
    price = models.IntegerField(default=0, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False, db_index=True)

    class Meta:
        abstract = False
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class VPN(Product):
    type = models.CharField(max_length=200, choices=VPNType.choices(), null=False, blank=False)
    duration = models.IntegerField(default=30, null=False, blank=True, help_text="Days")
    limit = models.IntegerField(default=0, null=False, blank=True, help_text="GiB")
    renewable = models.BooleanField(default=False, null=False, blank=False)
    
    class Meta:
        db_table = "vpn"
        verbose_name = "VPN"
        verbose_name_plural = "VPNs"



class Giftcard(Product):
    type = models.CharField(max_length=200, choices=GiftcardType.choices(), null=False, blank=False)
    country = models.CharField(max_length=2, choices=Country.choices(), null=False, blank=False)
    
    class Meta:
        db_table = "giftcard"
        verbose_name = "Giftcard"
        verbose_name_plural = "Giftcards"
