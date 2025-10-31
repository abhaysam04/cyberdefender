from django.db import models
from django.utils import timezone

class SecurityAlert(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Medium')
    reported_by = models.CharField(max_length=100, blank=True)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    date_reported = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.severity}] {self.title}"
