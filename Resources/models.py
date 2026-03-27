from django.db import models
from django.utils.text import slugify

class Library(models.Model):
    id = models.SlugField(primary_key=True, unique=True, editable=False, max_length=60)
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True, null=True)
    library_link = models.TextField(max_length=500)
    how_to_use = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # ✅ default TRUE

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def _generate_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1
        while Library.objects.filter(id=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.title)
            self.id = self._generate_unique_slug(base_slug)
        super().save(*args, **kwargs)