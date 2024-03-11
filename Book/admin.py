from django.contrib import admin
from .models import Sheets, SheetImage, Buyers, Order
# Register your models here.

admin.site.register(Buyers)

class SheetImageInline(admin.TabularInline):
    model = SheetImage

class SheetsAdmin(admin.ModelAdmin):
    inlines = [SheetImageInline]

admin.site.register(Sheets, SheetsAdmin)

admin.site.register(Order)