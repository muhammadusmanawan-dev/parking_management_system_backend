from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_spot', 'status', 'entry_time')

    list_filter = ('status', 'entry_time')
    
    search_fields = ('id', 'parking_spot__spot_number')
