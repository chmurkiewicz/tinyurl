from django.contrib import admin

from tinyurl.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "original_url")
    search_fields = list_display
    readonly_fields = ("id",)
