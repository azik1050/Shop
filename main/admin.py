from django.contrib import admin
from .models import Category, Product, AboutPage


class ProductInline(admin.StackedInline):
    extra = 0
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fields = (('name', 'slug'), 'description', 'text', 'image', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'total', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('price', 'total', 'is_active')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('category', ('title', 'slug'), 'description', ('price', 'total'), 'text', ('color', 'material'),   'created_at', 'image', 'is_active')
    search_fields = ('title',)
    search_help_text = 'Enter name of product'


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'changed_at')
    list_display_links = ('title',)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AboutPage, AboutPageAdmin)

