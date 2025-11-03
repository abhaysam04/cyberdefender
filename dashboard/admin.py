from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'date_reported', 'reported_by', 'source_ip')
    list_filter = ('severity', 'date_reported')
    search_fields = ('title', 'description')
    readonly_fields = ('date_reported',)

