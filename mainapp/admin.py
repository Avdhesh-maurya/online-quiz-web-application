from django.contrib import admin
from .models import Question

# Customize how Question appears in the admin panel
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "text", "answer")  # show these fields in list view
    list_filter = ("category",)                          # filter sidebar by category
    search_fields = ("text", "category")                 # enable search by text or category
    ordering = ("category", "id")                        # sort by category then id
