import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Library

@csrf_exempt
def bulk_create_libraries(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            if not isinstance(data, list):
                return JsonResponse({"error": "Expected a list of objects"}, status=400)

            created_items = []

            for item in data:
                library = Library(
                    title=item.get("title"),
                    description=item.get("description"),
                    library_link=item.get("library_link"),
                    how_to_use=item.get("how_to_use"),
                    is_active=True  # force TRUE
                )

                library.save()
                created_items.append(library.id)

            return JsonResponse({
                "message": "Data saved successfully",
                "created_ids": created_items
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)