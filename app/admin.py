from django.contrib import admin

from .models import *

admin.site.site_header = 'My Store'


# Register your models here.

class Menu(admin.ModelAdmin):
    list_display = ("id", "name", "sts")


class Category(admin.ModelAdmin):
    list_display = ("id", "name", "sts")


class PostImageAdmin(admin.StackedInline):
    model = productImage


@admin.register(product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ("id", "title", "sts", "create_at")
    list_per_page = 10
    class Meta:
        model = product


@admin.register(productImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# class Product(admin.ModelAdmin):
#     list_filter = [
#         "title",
#         "desc",
#         "menu"
#     ]
#     search_fields = (
#         "title",
#         "desc",
#     )
#
#     list_display = ("id", "menu", "category", "title", "desc", "img", "sts")


class Wishlist(admin.ModelAdmin):
    list_display = ("id", "user", "product")


class Viewerslist(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ('viewers', "product")
    list_display = ("id", "viewers", "product")


admin.site.register(menu, Menu)
admin.site.register(category, Category)
# admin.site.register(product)
admin.site.register(wishlist, Wishlist)
admin.site.register(count, Viewerslist)
