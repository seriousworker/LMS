from courses.forms import CourseFilterForm
from courses.forms import CreateCourseForm
from courses.forms import UpdateCourseForm
from courses.models import Course

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView


class ListCourseView(ListView):
    model = Course
    template_name = 'templates/courses/list.html'
    extra_context = {'title': 'List of courses'}

    def get_queryset(self):
        course = Course.objects.select_related('group_of_course')
        filter_form = CourseFilterForm(data=self.request.GET, queryset=course)

        return filter_form


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class DetailCourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
