from django.contrib import admin
from .models import Car, BillingInfo, Account

# Register your models here.
admin.site.register(Car)
admin.site.register(BillingInfo)
admin.site.register(Account)