from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import UpdateView


from groups.forms import CreateGroupForm
# from groups.forms import GroupFilterForm
from groups.forms import UpdateGroupForm
from groups.models import Group

from students.models import Student


# def get_group(request):
#     groups = Group.objects.select_related('headman')
#
#     filter_form = GroupFilterForm(data=request.GET, queryset=groups)
#     return render(request,
#                   template_name='templates/groups/list.html',
#                   context={
#                       'title': 'List of groups',
#                       'filter_form': filter_form,
#                   })


class ListGroupView(ListView):
    model = Group
    template_name = 'templates/groups/list.html'


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    return render(request, 'groups/detail.html', {'group': group})


class UpdateGroupView(UpdateView):
    model = Group
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')
        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        elif pk == 0:
            form.instance.headman = None
        form.save()

        return response


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
