from django.contrib import admin
from flats.models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "text")
