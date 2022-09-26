from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render     # noqa

from students.forms import CreateStudentForm
from students.models import Student
from students.utils import qs2html

from webargs.djangoparser import use_args
from webargs.fields import Str


def index(request):
    return HttpResponse('Welcome to the Learning Management System!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    html_form = ('\n'
                 '        <form method="get">\n'
                 '              <label for="first_name">First name:</label>\n'
                 '              <input type="text" id="first_name" name="first_name" value="John"><br><br>\n'
                 '              <label for="last_name">Last name:</label>\n'
                 '              <input type="text" id="last_name" name="last_name" placeholder="Doe"><br><br>\n'
                 '              <input type="submit" value="Submit">\n'
                 '        </form> \n'
                 '        ')

    html = qs2html(students)

    response = HttpResponse(html_form + html)
    return response


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = (f'\n'
                 f'        <form method="post">\n'
                 f'            <input type="hidden" name="csrfmiddlewaretoken" value="{token}"> \n'
                 f'            <table>    \n'
                 f'                {form.as_table()}\n'
                 f'            </table>\n'
                 f'            <input type="submit" value="Submit">\n'
                 f'        </form> \n'
                 f'    ')

    return HttpResponse(html_form)
