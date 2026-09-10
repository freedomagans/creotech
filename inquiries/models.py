from django.db import models

class Inquiry(models.Model):
    INQUIRY_TYPE_CHOICES = [
        ('contact', 'Contact'),
        ('start_project', 'Start Project')
    ]
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPE_CHOICES, default='contact')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    project_type = models.CharField(max_length=150, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.inquiry_type})"