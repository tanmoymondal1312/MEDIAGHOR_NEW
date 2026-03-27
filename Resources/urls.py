# urls.py
from django.urls import path
from . import views
from .api_views import bulk_create_libraries

app_name = 'resources'

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('<slug:id>/', views.library_detail, name='library_detail'),
    # ... other URLs
    
    path('api/libraries/bulk-create/', bulk_create_libraries),
]