from django.contrib import admin

from apps.results import models


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'created', 'updated',)
