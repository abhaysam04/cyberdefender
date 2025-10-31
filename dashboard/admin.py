from django.contrib import admin
from .models import SecurityAlert

@admin.register(SecurityAlert)
class SecurityAlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'date_reported')
    search_fields = ('title', 'description')
    list_filter = ('severity',)
