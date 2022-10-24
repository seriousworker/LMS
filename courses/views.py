from courses.forms import CourseFilterForm
from courses.forms import CreateCourseForm
from courses.forms import UpdateCourseForm
from courses.models import Course

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


def get_course(request):
    courses = Course.objects.all()

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)
    return render(request,
                  template_name='templates/courses/list.html',
                  context={
                      'title': 'List of courses',
                      'filter_form': filter_form,
                  })


def create_course(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/create.html', {'form': form})


def detail_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    return render(request, 'courses/detail.html', {'course': course})


def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'GET':
        form = UpdateCourseForm(instance=course)
    if request.method == 'POST':
        form = UpdateCourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': course})
