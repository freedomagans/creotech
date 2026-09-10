from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'inquiry_type', 'is_read', 'created_at')
    list_filter = ('inquiry_type', 'is_read')
    list_editable = ('is_read',)
    ordering = ('-created_at',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # Make all fields read-only except is_read for existing objects
            return [field.name for field in obj._meta.fields if field.name != 'is_read']
        return []