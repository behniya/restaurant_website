from accounts.models import MenuItem
from decimal import Decimal

class Cart():
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self , item , quantity):
        """
        Adding an updating the users cart session data
        """
        item_id = item.id

        if item_id not in self.cart:
            self.cart[item_id] = {'price' : str(item.price) , 'quantity' : int(quantity)}

        self.save()

    def __iter__(self):
        """
        Collect the item_id in the session data to querry the database 
        and return items
        """
        item_ids = self.cart.keys()
        items = MenuItem.objects.filter(id__in=item_ids)
        cart = self.cart.copy()

        for item in items:
            cart[str(item.id)]['item'] = item

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item 

    def __len__(self):
        """
        Get the cart data and count the quantity of items
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def delete(self , item):
        """
        Delete item from session data
        """
        item_id = str(item)

        if item_id in self.cart:
            del self.cart[item_id]
        
        self.save()

    def save(self):
        self.session.modified = True

    def add(self, item, quantity=1):
        """
        Add or update the cart with the given item and quantity.
        Quantity can be negative to decrease the amount.
        """
        item_id = str(item.id)

        if item_id in self.cart:
            self.cart[item_id]['quantity'] += int(quantity)
            
            # If the quantity goes to 0 or less, remove the item
            if self.cart[item_id]['quantity'] <= 0:
                del self.cart[item_id]
        else:
            if quantity > 0:
                self.cart[item_id] = {'price': str(item.price), 'quantity': int(quantity)}

        self.save()

