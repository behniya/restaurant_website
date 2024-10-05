from django.db import models
from django.conf import settings
from django.db import models
from accounts.models import MenuItem  # Import MenuItem from the accounts app

class ShoppingBox(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class BoxItem(models.Model):
    shopping_box = models.ForeignKey(ShoppingBox, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # This references MenuItem from accounts
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.quantity * self.item.price
