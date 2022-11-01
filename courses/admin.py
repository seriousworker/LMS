from courses.models import Course

from django.contrib import admin


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'course_title',
        'course_level',
        'course_place',
        'course_start',
    )
    list_display_links = list_display
    search_fields = (
        'course_title',
        'course_place',
        'course_start',
    )
    show_full_result_count = False
    list_per_page = 20
    fieldsets = (
        ('Title', {'fields': ('course_title',)}),
        ('Level', {'fields': ('course_level',)}),
        ('Teaching plan', {'fields': ('course_description',)}),
        ('Place', {'fields': ('course_place',)}),
        ('Dates', {'fields': (
            'course_start',
            'created_datetime',
            'updated_datetime',
        )}),
        ('Price', {'fields': ('course_price', 'course_price_currency')}),
        ('Conditions', {'fields': (
            'course_enrollment_condition',
            'course_graduation_condition',
        )})
    )
    readonly_fields = (
        'created_datetime',
        'updated_datetime',
    )


admin.site.register(Course, CourseAdmin)
