import re

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import AppSubscription, CourseRegistration  # Assuming you have an Application model
import json

@require_POST
@csrf_exempt
def app_form_view(request):
    """
    Handle application form submission with AJAX support
    """
    try:
        # Get form data
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        educational_qualification = request.POST.get('educational_qualification')
        programming_experience = request.POST.get('programming_experience', 'Beginner')
        message = request.POST.get('message', '')
        
        # Validate required fields
        if not all([full_name, age, phone_number, email, educational_qualification]):
            return JsonResponse({
                'success': False,
                'message': 'দয়া করে সব প্রয়োজনীয় তথ্য পূরণ করুন'
            }, status=400)
        
        
        # Create application record
        application = CourseRegistration.objects.create(
            full_name=full_name,
            age=age,
            phone_number=phone_number,
            email=email,
            educational_qualification=educational_qualification,
            programming_experience=programming_experience,
            message=message
        )
        
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'আপনার তথ্য সফলভাবে জমা হয়েছে! আমরা খুব শীঘ্রই আপনার সাথে যোগাযোগ করবো।',
                'application_id': application.id
            })
        else:
            # For regular form submission
            return render(request, 'success.html', {
                'message': 'আপনার তথ্য সফলভাবে জমা হয়েছে! আমরা খুব শীঘ্রই আপনার সাথে যোগাযোগ করবো।'
            })
            
    except Exception as e:
        print(f"Error in app_form_view: {e}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'দুঃখিত, কিছু সমস্যা হয়েছে। আবার চেষ্টা করুন।'
            }, status=500)
        else:
            return render(request, 'error.html', {
                'message': 'দুঃখিত, কিছু সমস্যা হয়েছে। আবার চেষ্টা করুন।'
            })
            
            
            
            
            
            
            
            
            
            
@require_POST
@csrf_exempt
def subscribe_app_notification(request):
    """
    API endpoint to handle app notification subscriptions
    """
    try:
        # Get email from POST data
        data = json.loads(request.body) if request.body else request.POST
        email = data.get('email', '').strip()
        
        # Validate email
        if not email:
            return JsonResponse({
                'success': False,
                'message': 'দয়া করে আপনার ইমেইল ঠিকানা দিন'
            }, status=400)
        
        # Email format validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return JsonResponse({
                'success': False,
                'message': 'দয়া করে একটি বৈধ ইমেইল ঠিকানা দিন'
            }, status=400)
        
        # Check if email already exists
        subscription, created = AppSubscription.objects.get_or_create(
            email=email,
            defaults={
                'ip_address': get_client_ip(request),
                'user_agent': request.META.get('HTTP_USER_AGENT', '')
            }
        )
        
        if created:
            # New subscription
            return JsonResponse({
                'success': True,
                'message': 'ধন্যবাদ! অ্যাপ লঞ্চের খবর আমরা আপনার ইমেইলে পাঠিয়ে দেবো।'
            })
        else:
            # Already subscribed
            return JsonResponse({
                'success': True,
                'message': 'আপনি ইতিমধ্যেই সাবস্ক্রাইব করেছেন! অ্যাপ লঞ্চের খবর পাবেন।'
            })
            
    except Exception as e:
        print(f"Error in subscribe_app_notification: {e}")
        return JsonResponse({
            'success': False,
            'message': 'দুঃখিত, কিছু সমস্যা হয়েছে। আবার চেষ্টা করুন।'
        }, status=500)

def get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip