from django.db import models
from django.utils.translation import gettext_lazy as _

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    class ToDoPriority(models.TextChoices):
        HIGH_PRIORITY = 'High', _('High Priority')
        LOW_PRIORITY = 'Low', _('Low Priority')
    priority = models.CharField(
        max_length=5, 
        choices=ToDoPriority.choices,
        default=ToDoPriority.HIGH_PRIORITY
        )

    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title










