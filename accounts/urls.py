from django.urls import path
from .views import (SignUpView , CustomLogoutView , ProfileUpdateView ,
                     CustomPasswordChangeView , CustomLoginView , MenuItemListView , MenuItemDetailView)
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/' , SignUpView.as_view() , name = 'signup'),
    path('logout/' , CustomLogoutView.as_view() , name = 'logout'),
    path('login/' , CustomLoginView.as_view() , name = 'login'),
    path('profile/' , ProfileUpdateView.as_view() , name = 'profile'),
    path('password/change/' , CustomPasswordChangeView.as_view() , name = 'password_change'),
    path('password/change/done/' , PasswordChangeDoneView.as_view(template_name = 'registration/password_change_done.html') , 
         name='password_change_done'),
    path('password_reset/' , auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html') , name='password_reset'),
    path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html') , name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html') , name='password_reset_confirm'),
    path('password_reset_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html') , name='password_reset_complete'),
    path('menu/' , MenuItemListView.as_view() , name='menu_list'),
    path('menu/<int:pk>/' , MenuItemDetailView.as_view() , name='menu_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
