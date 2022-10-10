from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from groups.forms import CreateGroupForm
from groups.forms import GroupFilterForm
from groups.forms import UpdateGroupForm
from groups.models import Group


def get_group(request):
    groups = Group.objects.all()

    filter_form = GroupFilterForm(data=request.GET, queryset=groups)
    return render(request,
                  template_name='templates/groups/list.html',
                  context={
                      'title': 'List of groups',
                      'filter_form': filter_form,
                  })


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    return render(request, 'groups/detail.html', {'group': group})


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    if request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
