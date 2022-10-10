from django import forms

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_description',
            'start_date',
            'end_date',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass
