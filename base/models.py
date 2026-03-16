from django.db import models
from django.utils import timezone
from datetime import timedelta


def default_deadline():
    return timezone.now() + timedelta(days=1)


# =============== Todo model =============== 
class Todo(models.Model):

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", 'Medium'),
        ("high", "High"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)

    priority = models.CharField(max_length=10, default="medium", choices=PRIORITY_CHOICES) 

    deadline = models.DateField(default=default_deadline)

    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title