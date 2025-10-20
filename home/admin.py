# home/admin.py

from django.contrib import admin
from .models import *

# Generic admin for models that don't need special handling
@admin.register(
    Experience,
    Project,
    ProblemSolving,
    Achievement,
    Leadership,
    Certification,
    Blog,
    Recommendation,
    Contact
)
class UniversalAdmin(admin.ModelAdmin):
    pass

# Special admin for Education (to support GPA/CGPA label)
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'grade', 'grade_label', 'study_period')
    list_filter = ('institution', 'grade_type')
    search_fields = ('degree', 'institution')

# Special admin for Publication (to support DOI & Publisher)
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference', 'year', 'status', 'publisher', 'doi_link')
    list_filter = ('year', 'status', 'publisher')
    search_fields = ('title', 'authors', 'conference')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'name')