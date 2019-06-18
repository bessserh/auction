from django.contrib import admin
from django.contrib.admin import ModelAdmin

from auction.models import Photo, Item


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    def __str__(self):
        return self.photo



@admin.register(Item)
class ItemAdmin(ModelAdmin):
    pass
