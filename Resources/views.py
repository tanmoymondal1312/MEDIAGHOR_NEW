# views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Library

def library_list(request):
    """
    View to display all libraries with search and pagination
    """
    # Get search query from URL parameters
    search_query = request.GET.get('search', '')
    
    # Base queryset - only active libraries
    libraries = Library.objects.filter(is_active=True)
    
    # Apply search filter if query exists
    if search_query:
        libraries = libraries.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        ).distinct()
    
    # Order by latest first
    libraries = libraries.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(libraries, 12)  # Show 12 libraries per page
    page = request.GET.get('page', 1)
    
    try:
        libraries_page = paginator.page(page)
    except PageNotAnInteger:
        libraries_page = paginator.page(1)
    except EmptyPage:
        libraries_page = paginator.page(paginator.num_pages)
    
    context = {
        'libraries': libraries_page,
        'paginator': paginator,
        'search_query': search_query,
    }
    
    return render(request, 'resources_home.html', context)


def library_detail(request, id):
    """
    View to display library/resource detail page
    """
    # Get the main library object or return 404
    library = get_object_or_404(Library, id=id, is_active=True)
    
    # Get recommended libraries (latest 5 active libraries, excluding current)
    recommended_libraries = Library.objects.filter(
        is_active=True
    ).exclude(
        id=library.id
    ).order_by('-created_at')[:5]
    
    context = {
        'library': library,
        'recommended_libraries': recommended_libraries,
    }
    
    return render(request, 'resources_details.html', context)