from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'document', 'perfomance_card', 'created_at', 'updated_at']
    list_filter = [ 'created_at', 'updated_at']
    list_editable = ['document', 'perfomance_card']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

