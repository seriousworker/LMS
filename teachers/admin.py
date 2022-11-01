from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'occupation',
        'working_place',
        'full_salary',
    )
    list_display_links = list_display
    search_fields = (
        'first_name',
        'last_name',
        'occupation',
        'working_place',
    )
    show_full_result_count = False
    list_per_page = 20
    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Birthday', {'fields': ('birthday', 'age')}),
        ('Company', {'fields': ('occupation', 'working_place')}),
        ('Finance', {'fields': ('salary',)}),
        ('Contact data', {'fields': (
            'email',
            'phone',
            'linkedin',
            'telegram',
            'facebook',
            'youtube',
            'instagram',
        )}),
    )

    def full_salary(self, instance):
        if instance.salary:
            return f'{instance.salary} UAH'

    full_salary.short_description = 'Salary'
    full_salary.admin_order_field = 'salary'

    def age(self, instance):
        return f'{instance.get_age()} y.o.'

    readonly_fields = ('age',)
    age.short_description = 'age'


admin.site.register(Teacher, TeacherAdmin)
