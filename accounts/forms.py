from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser , MenuItem

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name' , 'last_name' , 'email', 'phone_number', 'address']
        exclude = ['password'] 

        # Override the init method to remove the password help text and field
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields['password'].widget = forms.HiddenInput()  # Hide the password field
            self.fields['password'].label = ''  # Remove the label
            self.fields['password'].help_text = ''  # Remove the help text

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name' , 'description' , 'price' , 'image' , 'category']