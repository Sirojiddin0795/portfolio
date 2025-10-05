from django.contrib import admin
from .models import Project, Skill, Lesson, Post, Contact, HomePageContent

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'profession', 'bio', 'profile_image', 'banner_image', 'hire_me_link')
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'github_url', 'instagram_url')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'icon', 'created_at']
    list_filter = ['level']
    search_fields = ['title']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
