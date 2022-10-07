
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from teachers.forms import CreateTeacherForm
from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_teacher(request, args):
    teachers = Teacher.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(request=request,
                  template_name='templates/teachers/list.html',
                  context={
                      'title': 'List of teachers',
                      'teachers': teachers,
                  })


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    return render(request, 'teachers/detail.html', {'teacher': teacher})


def create_teacher(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

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


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

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
