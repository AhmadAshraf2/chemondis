from django.contrib import admin
from .models import Slot


class SlotAdmin(admin.ModelAdmin):
    """
    creating Interview admin class to register for admin panel access
    """
    list_display = ('start_date', 'end_date', 'user')
    list_filter = ('user',)


admin.site.register(Slot, SlotAdmin)