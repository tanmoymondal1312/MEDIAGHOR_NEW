from django.urls import path
from . import views

app_name = 'Users'  # Replace with your app name

urlpatterns = [
    # Function-based view
    path('app-form/', views.app_form_view, name='app_form'),
    path('subscribe-app/', views.subscribe_app_notification, name='subscribe_app'),
    
    # OR Class-based view (uncomment if using class-based)
    # path('app-form/', views.CourseRegistrationCreateView.as_view(), name='app_form'),
]