from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login',views.Login,name='login'),
    path('register',views.Register,name='register'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html') , name='password-reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html') , name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html') , name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html' ) , name='password_reset_complete'),
    
    #path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

]