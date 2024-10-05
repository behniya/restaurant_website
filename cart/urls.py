from django.urls import path
from .views import cart_summary , cart_add , cart_delete , cart_update_quantity

urlpatterns = [
    path('', cart_summary, name='cart_summary'),
    path('add/' , cart_add , name='cart_add'),
    path('delete/' , cart_delete , name='cart_delete'),
    path('cart/update-quantity/', cart_update_quantity, name='cart_update_quantity'),
]