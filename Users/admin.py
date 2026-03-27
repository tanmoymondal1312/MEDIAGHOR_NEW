from time import timezone

from django.contrib import admin
from .models import AppSubscription, CourseRegistration

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'age', 'educational_qualification', 'programming_experience', 'created_at')
    list_filter = ('educational_qualification', 'programming_experience', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('ব্যক্তিগত তথ্য', {
            'fields': ('full_name', 'age', 'phone_number', 'email')
        }),
        ('শিক্ষাগত তথ্য', {
            'fields': ('educational_qualification', 'programming_experience')
        }),
        ('অতিরিক্ত তথ্য', {
            'fields': ('message', 'created_at', 'updated_at')
        }),
    )
    
    
    
@admin.register(AppSubscription)
class AppSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_notified', 'notified_at')
    list_filter = ('is_notified', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at', 'ip_address', 'user_agent')
    
    fieldsets = (
        ('Subscription Info', {
            'fields': ('email', 'subscribed_at', 'is_notified', 'notified_at')
        }),
        ('Technical Info', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_notified']
    
    def mark_as_notified(self, request, queryset):
        """Admin action to mark selected subscriptions as notified"""
        updated = queryset.update(is_notified=True, notified_at=timezone.now())
        self.message_user(request, f'{updated} subscription(s) marked as notified.')
    mark_as_notified.short_description = "Mark selected as notified"
