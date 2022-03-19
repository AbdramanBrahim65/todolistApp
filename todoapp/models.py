from django.db import models
from datetime import datetime
# Create your models here.

class TacheModel(models.Model):
    tache=models.CharField(max_length=400,null=True)
    date_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tache
    class Meta:
        ordering = ["-date_add"]
