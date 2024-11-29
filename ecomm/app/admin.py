from django.contrib import admin
from . models import Product, Customer, Cart, Wishlist, Comment
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price','category', 'product_image' ]

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'firstname','lastname','city', 'mobile', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']


#@admin.register(OrderPlaced)
#class OrderPlacedModelAdmin(admin.ModelAdmin):

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'product']

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment']

