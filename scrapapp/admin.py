from django.contrib import admin
from scrapapp.models import Scraps,Category


@admin.register(Scraps)
class scrapModelAdmin(admin.ModelAdmin):
    list_display=["id","name","user","category","price","location","image"]

@admin.register(Category)
class scrapModelAdmin(admin.ModelAdmin):
    list_display=["id","name"]


