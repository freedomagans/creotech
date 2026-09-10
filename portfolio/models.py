from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    client_name = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    cover_image = models.ImageField(upload_to='portfolio/covers/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"