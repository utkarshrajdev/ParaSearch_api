from django.contrib import admin
from .models import CustomUser, Paragraph, Word

# Register your models here.
admin.site.register(CustomUser)

@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['text']

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'paragraph']
    search_fields = ['word']
