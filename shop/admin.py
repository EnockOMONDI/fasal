from django.contrib import admin
from .models import Category, Student, Media, Team


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'perfomance_card', 'document','brief_story' , 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['document', 'perfomance_card']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Student, StudentAdmin,)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Media, MediaAdmin,)



class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'brief_description', 'position']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Team, TeamAdmin,)


