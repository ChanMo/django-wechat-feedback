from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('member', 'type', 'content', 'is_view', 'created')
    list_filter = ('created', 'is_view')

admin.site.register(Feedback, FeedbackAdmin)
