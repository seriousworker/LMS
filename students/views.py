from django.http import HttpResponse
from django.shortcuts import render     # noqa

from students.models import Student


def index(request):
    students = Student.objects.all()
    s = '<table>'

    for student in students:
        s += f'<tr><td>{student.first_name}</td><td>{student.last_name}</td><td>{student.email}</td></tr><br>'

    s += '<table>'
    response = HttpResponse(s)
    return response

