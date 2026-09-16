from django.contrib import admin
from .models import Experience, Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "started_at", "ended_at", "is_ongoing", "started_at")
    list_filter = ("category",)
    search_fields = ("title", "description")
    readonly_field = ("id")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency")
    list_filter = ("category", "proficiency")
    search_fields = ("name", "description")
    readonly_fields = ("id",)

