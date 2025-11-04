from django.contrib import admin
from .models import Category, Quiz, Question, Result

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "total_time", "created_at")
    list_filter = ("category",)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("quiz", "text", "correct_option")
    search_fields = ("text",)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "max_score", "taken_at")
    list_filter = ("quiz", "taken_at")
