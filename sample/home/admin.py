from django.contrib import admin

# Register your models here.
from .models import Departments,Booking,Doctors
admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'p_name', 'p_phone', 'p_email', 'doc_name','booking_date', 'booked_on' )

admin.site.register(Booking, BookingAdmin)

