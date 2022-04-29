from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("Title", max_length=200)
    done = models.BooleanField(default=False)
    date_time = models.DateTimeField("Date & Time", auto_now_add=True)
