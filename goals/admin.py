from django.contrib import admin
from .models import Goal

# Register your models here.
admin.site.register(Goal)

# from django.contrib import admin
# from goals.models import Goal
#
# # Register your models here.
# class GoalModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'updated', 'timestamp']
#     list_display_links = ['updated']
#     list_editable = ['title']
#     list_filter = ['updated', 'timestamp']
#     search_fields = ['title', 'content']
#
#     class Meta:
#         model = Goal
#
# admin.site.register(Goal, GoalModelAdmin)
