# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.models import LogEntry


class HistoryAdmin(admin.ModelAdmin):
    model = LogEntry

    list_display = ('user', 'action_time', 'change_message', 'content_object')
    list_filter = ('user', )
    date_hierarchy = 'action_time'

    def content_object(self, obj):
        return obj.content_object
    content_object.admin_order_field = 'object_id'

admin.site.register(LogEntry, HistoryAdmin)