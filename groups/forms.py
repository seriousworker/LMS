from django import forms

from django_filters import FilterSet

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(GroupBaseForm):
    from students.models import Student

    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.select_related('group'),
        required=False,
    )

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False,
        )
        self.fields['headman_field'].choices.insert(0, (0, '---------'))

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
            'headman',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'start_date': ['exact'],
            'end_date': ['exact'],
        }
