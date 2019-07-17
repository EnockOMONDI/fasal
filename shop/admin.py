from django.contrib import admin
from .models import Category, Student, Media, Team


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'document', 'perfomance_card', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['document', 'available', 'perfomance_card']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Student, ProductAdmin,)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Media, MediaAdmin,)



class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'brief_description', 'position']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Team, TeamAdmin,)


