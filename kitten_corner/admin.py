from django.contrib import admin

from kitten_corner.models import Kitten


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    search_fields = ("name", "age")
    list_display = ("name", "age")
    ordering = ("name",)
