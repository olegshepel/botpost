from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'created_by', 'description',
    )

    list_filter = (
        'created_by', 'description'
    )

    search_fields = (
        'created_by__email', 'description'
    )
