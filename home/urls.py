from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('booking',booking,name="booking"),
    # path('login',login,name="login"),
    path('testimonial',testimonial,name="testimonial"),
    path('room',room,name="room"),
    path('contact',contact,name="contact"),
    path('team',team,name="team"),
    path('service',service,name="service"), 
    
]