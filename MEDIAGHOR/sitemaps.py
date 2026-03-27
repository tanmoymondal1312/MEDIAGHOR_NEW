from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['home', 'about', 'resources:library_list']

    def location(self, item):
        try:
            return reverse(item)
        except:
            return None