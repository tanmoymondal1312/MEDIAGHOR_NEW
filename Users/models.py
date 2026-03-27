from time import timezone

from django.db import models

class CourseRegistration(models.Model):
    # Qualification choices
    SSC = 'SSC'
    HSC = 'HSC'
    BACHELOR = 'Bachelor'
    MASTERS = 'Masters'
    OTHER = 'Other'
    
    QUALIFICATION_CHOICES = [
        (SSC, 'এসএসিি'),
        (HSC, 'এইচএসসি'),
        (BACHELOR, 'স্নাতক'),
        (MASTERS, 'স্নাতকোত্তর'),
        (OTHER, 'অন্যান্য'),
    ]
    
    # Experience choices
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    
    EXPERIENCE_CHOICES = [
        (BEGINNER, 'শুরু করছি'),
        (INTERMEDIATE, 'মধ্যম'),
        (ADVANCED, 'উন্নত'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name='পূর্ণ নাম')
    age = models.PositiveIntegerField(verbose_name='বয়স')
    phone_number = models.CharField(max_length=20, verbose_name='ফোন নাম্বার')
    email = models.EmailField(verbose_name='ইমেইল')
    educational_qualification = models.CharField(
        max_length=20,
        choices=QUALIFICATION_CHOICES,
        verbose_name='শিক্ষাগত যোগ্যতা'
    )
    programming_experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default=BEGINNER,
        verbose_name='প্রোগ্রামিং অভিজ্ঞতা'
    )
    message = models.TextField(blank=True, null=True, verbose_name='বার্তা বা প্রশ্ন')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='যোগদানের তারিখ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='শেষ পরিবর্তনের তারিখ')
    
    class Meta:
        verbose_name = 'কোর্স রেজিস্ট্রেশন'
        verbose_name_plural = 'কোর্স রেজিস্ট্রেশন সমূহ'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"
    
    
    
    

class AppSubscription(models.Model):
    """
    Model to store email subscriptions for app launch notifications
    """
    email = models.EmailField(unique=True, max_length=254)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_notified = models.BooleanField(default=False, help_text="Whether notification email has been sent")
    notified_at = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, help_text="Browser/Device information")
    
    class Meta:
        verbose_name = "App Subscription"
        verbose_name_plural = "App Subscriptions"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return f"{self.email} - Subscribed at {self.subscribed_at}"
    
    def mark_as_notified(self):
        """Mark this subscription as notified"""
        self.is_notified = True
        self.notified_at = timezone.now()
        self.save()