from core.utils import clean_phone_number

from django import forms

from django_filters import FilterSet

from teachers.models import Teacher


class BaseTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
            'occupation',
            'working_place',
            'linkedin',
            'telegram',
            'facebook',
            'youtube',
            'instagram',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class CreateTeacherForm(BaseTeacherForm):
    class Meta(BaseTeacherForm.Meta):
        pass

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        titled_value = value.title()

        return titled_value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        titled_value = value.title()

        return titled_value

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        valid_number = clean_phone_number(value)

        return valid_number


class UpdateTeacherForm(BaseTeacherForm):
    class Meta(BaseTeacherForm.Meta):
        pass


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
            'working_place': ['exact'],
        }
