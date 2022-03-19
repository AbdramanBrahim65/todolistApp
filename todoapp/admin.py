from django.contrib import admin
from .models import TacheModel
# Register your models here.

class AdminTache(admin.ModelAdmin):
    list_tache = ('tache','date_add')


admin.site.register(TacheModel, AdminTache)