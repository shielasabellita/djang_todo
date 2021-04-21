from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class ToDo(models.Model):
    todo = models.CharField(max_length=60)
    is_done = models.CharField(max_length=1)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )