from django.db import models
from django.utils import timezone


# make migrations whenever models are changed - migrations update the database!
# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def completed(self):
        return self.completed_date is not None

    def complete(self):
        self.completed_date = timezone.now()

    def __str__(self):
        return self.text


