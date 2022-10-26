from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'group_name',
        'course',
        'start_date',
        'end_date',
    )
    list_display_links = list_display
    search_fields = (
        'group_name',
        'course',
    )
    show_full_result_count = False
    list_per_page = 20
    fieldsets = (
        ('Title', {'fields': ('group_name',)}),
        ('Course', {'fields': ('course',)}),
        ('Dates', {'fields': (
            'start_date',
            'end_date',
            'created_datetime',
            'updated_datetime',
        )}),
        ('Students', {'fields': ('headman',)})
    )
    readonly_fields = (
        'created_datetime',
        'updated_datetime',
    )


admin.site.register(Group, GroupAdmin)
