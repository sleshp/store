from django.contrib import admin

from feedback.models import Feedback, KnowledgeBase, ReferenceMaterial


@admin.register(Feedback)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'text', 'rating', 'status')


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'category')


@admin.register(ReferenceMaterial)
class ReferenceMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'content')
