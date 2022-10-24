from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from teachers.forms import CreateTeacherForm
from teachers.forms import TeacherFilterForm
from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'templates/teachers/list.html'
    extra_context = {'title': 'List of teachers'}

    def get_queryset(self):
        teachers = Teacher.objects.select_related()
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)

        return filter_form


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = UpdateTeacherForm


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
