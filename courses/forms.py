from courses.models import Course

from django import forms

from django_filters import FilterSet


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        help_texts = {
            'course_duration': 'lessons',
            'course_enrollment_condition': 'points',
            'course_graduation_condition': 'points',
        }
        widgets = {
            'course_start': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class UpdateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_title': ['icontains'],
            'course_place': ['exact'],
            'course_start': ['icontains'],
        }
