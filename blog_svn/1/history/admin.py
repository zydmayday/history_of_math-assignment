from django.contrib import admin

from history.models import History

class HistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(History, HistoryAdmin)