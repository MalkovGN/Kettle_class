from django.contrib import admin

from .models import LogModel


class Admin(admin.ModelAdmin):
    readonly_fields = ('time_start', 'time_end', 'date',)


admin.site.register(LogModel, Admin)
