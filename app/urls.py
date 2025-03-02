from django.urls import path
from app import views

urlpatterns =[
    path('',views.index,name="index"),
    path('Register',views.Register,name="Register"),
    path('hlogin',views.handlelogin,name="handlelogin"),
    path('contact',views.contact,name='contact'),
    path('agent',views.agent,name="agent"),
    path('about',views.about,name="about"),
    path('property',views.property,name="property"),
    path('submit-property',views.submit_property,name="submit_property"),
    path('hlogout',views.handlelogout,name="handlelogout"),
    path('myproperty',views.myproperty,name="myproperty"),
    path('edit_property/<id>',views.edit_property,name="edit_property"),
    path('delete_property/<id>',views.delete_property,name="delete_property"),
    path('search',views.search,name="search"),
    path('view_details/<id>',views.view_details,name="view_details"),
    path('installment',views.installment,name="installment"),
    path('booking-now',views.booking_now,name="booking_now"),

  ]