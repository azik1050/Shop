from django.contrib import admin
from .models import Category, Product, AboutPage



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'total', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('price', 'total', 'is_active')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'changed_at')
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AboutPage, AboutPageAdmin)

