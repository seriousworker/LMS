from django.contrib import admin

from groups.models import Group


class StudentInlineTable(admin.TabularInline):
    from students.models import Student

    model = Student
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    extra = 0
    readonly_fields = fields

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


@admin.register(Group)
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
        ('Students', {'fields': ('headman',)}),
    )
    readonly_fields = (
        'created_datetime',
        'updated_datetime',
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False

        form.base_fields['course'].widget.can_add_related = False
        form.base_fields['course'].widget.can_change_related = False

        return form

    inlines = [StudentInlineTable]
