from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", admin_login, name="admin_login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", Logoutpage, name="logout"),
    path("globalsetting/", globalsetting, name="globalsetting"),
    path("contact_us/", contact_us, name="contact_us"),
    path("delete/<int:pk>/", delete_contact, name="delete"),
    path("main_navigation/<int:parent_id>/", main_navigation, name="main_navigation"),
    path("main_navigation/", main_navigation, name="main_navigation"),
    path("navigation/", navigation_list, name="navigation"),
    path("navigation/<int:parent_id>/", navigation_list, name="navigation"),
    path("update/<int:pk>/", update, name="update"),
    path("delete_nav/<int:pk>/", delete_nav, name="delete_nav"),
    path("bookings/", bookings, name="bookings"),
    path("delete_bookings/<int:pk>/", delete_bookings, name="delete_bookings"),
    path('room_details/',room_details,name='room_details'),
    path('room_create/',room_create,name='room_create'),
    path('room_update/<int:pk>/',room_update,name='room_update'),
    path('room_delete/<int:pk>/',room_delete,name='room_delete'),
]
