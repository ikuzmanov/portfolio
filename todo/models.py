from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    due_date = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
