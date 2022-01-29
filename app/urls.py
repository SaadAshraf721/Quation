from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
    path('logout/', logout),
    path('login/', login),
    path('register/', register),
    path('product_detail/<int:id>', product_detail),
    path('products/<int:id>', products),
    path('wishlist/', wishlists),
    path('search/', search),
    path('addwishlist/<int:sid>', addwishlist),
    path('delwishlist/<int:ssid>', deletewishlist),
    path('404/', E404),
]
# handler404 = "app.entry_not_found"
