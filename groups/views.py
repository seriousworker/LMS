from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

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
                  template_name='groups/list.html',
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
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = (f'\n'
                 f'        <form method="post">\n'
                 f'            <input type="hidden" name="csrfmiddlewaretoken" value="{token}"> \n'
                 f'            <table>    \n'
                 f'                {form.as_table()}\n'
                 f'            </table>\n'
                 f'            <input type="submit" value="Create">\n'
                 f'        </form> \n'
                 f'    ')

    return HttpResponse(html_form)


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    return render(request, 'groups/detail.html', {'group': group})


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    if request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = (f'\n'
                 f'        <form method="post">\n'
                 f'            <input type="hidden" name="csrfmiddlewaretoken" value="{token}"> \n'
                 f'            <table>    \n'
                 f'                {form.as_table()}\n'
                 f'            </table>\n'
                 f'            <input type="submit" value="Update">\n'
                 f'        </form> \n'
                 f'    ')

    return HttpResponse(html_form)
