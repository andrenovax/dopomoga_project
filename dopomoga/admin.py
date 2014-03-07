from django.contrib import admin
from dopomoga.models import *


class ProjectInneedAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_started', 'project_author', 'phone')


class CommentInline(admin.TabularInline):
    model = ProjectHelperComment
    extra = 3


class ReviewInline(admin.StackedInline):
    model = ProjectHelperReview
    extra = 1


class ProjectHelperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'reports']}),
        ('relations', {'fields': ['project_author', 'resource', 'cause']}),
        ('description', {'fields': ['descr', 'picture', 'website', 'phone', 'how_to_help', 'place'], 'classes': ['collapse']}),
        ('status', {'fields': ['res_qnt', 'funded', 'votes']}),
    ]
    inlines = [CommentInline, ReviewInline]


admin.site.register(ProjectInneed, ProjectInneedAdmin)
admin.site.register(ProjectInneedReview)
admin.site.register(ProjectInneedComment)

admin.site.register(ProjectHelper, ProjectHelperAdmin)
admin.site.register(ProjectHelperReview)
admin.site.register(ProjectHelperComment)

admin.site.register(Resource)
admin.site.register(ResourceComment)

admin.site.register(Cause)
admin.site.register(CauseComment)

admin.site.register(UserProfile)
admin.site.register(UserProfileComment)

admin.site.register(UserInneedProfile)
admin.site.register(UserInneedComment)
