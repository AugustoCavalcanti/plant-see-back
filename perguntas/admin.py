from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'img_url')
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]