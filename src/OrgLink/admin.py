from django.contrib import admin

from OrgLink.models import OrgLink

@admin.register(OrgLink)
class OrgLinksAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'description',
        'url',
        'slug',
    ]
