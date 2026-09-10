from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured', 'order')