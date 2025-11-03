from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Low')
    date_reported = models.DateTimeField(auto_now_add=True)
    reported_by = models.CharField(max_length=100, default='Auto-Feed')
    source_ip = models.CharField(max_length=45, blank=True, null=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return f"[{self.severity}] {self.title}"

    class Meta:
        ordering = ['-date_reported']
