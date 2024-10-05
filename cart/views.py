from django.shortcuts import render , get_object_or_404
from .cart import Cart
from accounts.models import MenuItem
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    return render(request , 'cart_summary.html' , {'cart' : cart})

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'POST':
        item_id = int(request.POST.get('itemid'))
        quantity = int(request.POST.get('quantity'))  # Get quantity from the request
        item = get_object_or_404(MenuItem, id=item_id)
        
        cart.add(item=item, quantity=quantity)  # Pass quantity to the cart's add method
        
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        item_id = int(request.POST.get('itemid'))
        cart.delete(item=item_id)
        
        response = JsonResponse({'success': True})
        return response
    else:
        response = JsonResponse({'success': False})
        return response

def cart_update_quantity(request):
    cart = Cart(request)
    
    if request.POST.get('action') in ['increase', 'decrease']:
        item_id = int(request.POST.get('itemid'))
        item = get_object_or_404(MenuItem, id=item_id)
        
        if request.POST.get('action') == 'increase':
            cart.add(item=item, quantity=1)  # Increase by 1
        else:
            cart.add(item=item, quantity=-1)  # Decrease by 1
        
        item_quantity = cart.cart[str(item.id)]['quantity']
        
        if item_quantity == 0:
            cart.delete(item_id)  # If quantity is 0, remove item
        
        response = JsonResponse({'success': True, 'quantity': item_quantity})
        return response

    return JsonResponse({'success': False})