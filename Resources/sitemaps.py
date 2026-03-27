from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Library


class LibrarySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Library.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/resources/{obj.id}"