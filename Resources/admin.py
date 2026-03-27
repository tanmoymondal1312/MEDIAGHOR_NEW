from django.contrib import admin
from .models import Library

# Register Library model with simple configuration
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    """
    Simple admin configuration for Library model
    """
    # What fields to display in the list view
    list_display = ('title', 'created_at', 'updated_at')
    





