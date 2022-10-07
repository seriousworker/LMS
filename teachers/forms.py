from django import forms

from teachers.models import Teacher
from teachers.utils import clean_phone_number


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'subject',
            'email',
            'phone',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

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


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'subject',
            'email',
            'phone',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
