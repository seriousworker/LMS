from django import forms

from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_description'
        ]


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_creation_date',
            'group_description'
        ]
        widgets = {
            'group_creation_date': forms.DateInput(attrs={'type': 'date'})
        }
