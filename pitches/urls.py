from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.pitches,name='pitches'),
    path('<int:id>',views.pitche_page,name='pitche'),
    path('delate-booking/<int:id>',views.delateBooking,name='delate-booking'),
    #path('check_activate/',views.check_activate,name='check_activate')

]