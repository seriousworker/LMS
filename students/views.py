from django.http import HttpResponse
from django.shortcuts import render     # noqa

from students.models import Student


def index(request):
    students = Student.objects.all()
    s = '<table>'

    for student in students:
        s += f'<tr><td>{student.first_name}</td>' \
             f'<td>{student.last_name}</td>' \
             f'<td>{student.email}</td>' \
             f'</tr>'

    s += '</table>'
    response = HttpResponse(s)
    return response
