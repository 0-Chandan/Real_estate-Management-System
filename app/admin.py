from django.contrib import admin
from .models import Contacts,Submitproperty,Feedback,Booking
# Register your models here.
# Feedback,Booking.
admin.site.register(Submitproperty)
admin.site.register(Contacts)
admin.site.register(Feedback)
admin.site.register(Booking)