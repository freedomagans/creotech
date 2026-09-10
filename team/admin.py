from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'order')