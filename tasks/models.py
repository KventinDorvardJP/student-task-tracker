from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "Todo"),
        ("doing", "Doing"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="todo",
    )

    def __str__(self):
        return f"{self.title} ({self.status})"