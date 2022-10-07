from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from groups.forms import CreateGroupForm
from groups.forms import UpdateGroupForm
from groups.models import Group

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'group_name': Str(required=False)
    },
    location='query'
)
def get_group(request, args):
    groups = Group.objects.all()

    if len(args) != 0 and args.get('group_name'):
        groups = groups.filter(
            Q(group_name=args.get('group_name', ''))
        )

    return render(request,
                  template_name='templates/groups/list.html',
                  context={
                      'title': 'List of groups',
                      'groups': groups
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

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
