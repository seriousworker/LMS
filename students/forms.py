from django import forms

from students.models import Student
from students.utils import clean_phone_number


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        # method title, in case of multi words name, capitalize every word and after apostrophe
        titled_value = value.title()

        return titled_value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        # method title, in case of multi words name, capitalize every word and after apostrophe
        titled_value = value.title()

        return titled_value

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        valid_number = clean_phone_number(value)

        return valid_number


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
