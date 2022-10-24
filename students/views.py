from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from students.forms import CreateStudentForm
from students.forms import StudentFilterForm
from students.forms import UpdateStudentForm
from students.models import Student


def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)
    return render(request=request,
                  template_name='templates/students/list.html',
                  context={
                      'filter_form': filter_form
                  })


def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    return render(request, 'students/detail.html', {'student': student})


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/update.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
