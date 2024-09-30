from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150 , blank=True , null=True)
    last_name = models.CharField(max_length=150 , blank=True , null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

class MenuItem(models.Model):

    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('sushi_roll', 'Sushi Roll'),
        ('main_course', 'Main Course'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    image = models.ImageField(upload_to='menu_images/' , null=True , blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES , default='starter')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image after saving it
        if self.image:
            img = Image.open(self.image.path)

            # Define the max size (you can adjust this)
            max_size = (300, 300)

            # Resize the image while maintaining the aspect ratio
            img.thumbnail(max_size)

            # Save the image back
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('item_detail' , kwargs={'pk':self.pk})