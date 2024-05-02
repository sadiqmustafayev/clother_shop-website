from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from core.models import *
from modeltranslation.admin import TranslationAdmin




admin.site.site_header = 'MaleFashion Admin'

# class ImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1

class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'category_name', 'size_names', 'currency', 'get_discount_price', ) 
    search_fields = ('name', 'price', 'category__name', 'color__name')
    list_filter = ('category', 'color')
    readonly_fields = ('like',)
    fields = ('name', 'price', 'category', 'color', 'size', 'currency', 'images', 'like', 'is_active')
    # ordering  = ('-created_at')
    # inlines = [ImageInline]

    
    def get_image_display(self, obj):
        return obj.image.url if obj.image else None

    get_image_display.short_description = 'Image'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ('like', 'is_active')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_active=True)
    
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            obj.is_active = False
            obj.save()
        else:
            obj.delete()
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_active:
            return True
        return False

    def size_names(self, obj):
        return ", ".join([size.name for size in obj.size.all()])

    def category_name(self, obj):
        return obj.category.name

    size_names.short_description = "Sizes"
    category_name.short_description = "Category"

class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'desription')
    list_filter = ('created_at',)
    fields = ('title', 'desription', 'image', 'aforism', 'author', 'is_active')
    ordering = ('-created_at', 'is_active',)


@admin.register(ShopComments)
class ShopCommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'comment')
    search_fields = ('name', 'email', 'comment')
    list_filter = ('name', 'email')


@admin.register(Color)
class ColorAdmin(TranslationAdmin):
    list_display = ('name',)  
    search_fields = ('name',)
    


admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(Color, ColorAdmin)
admin.site.register(Category)
admin.site.register(Currency)
# admin.site.register(Color, TranslationAdmin)
admin.site.register(Size)
admin.site.register(ContactUs)
admin.site.register(Setting)
admin.site.register(ShopImage)
admin.site.register(ShopCategory)
admin.site.register(Contact)
admin.site.register(FAQ)