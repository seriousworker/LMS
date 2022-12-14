from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from students.forms import CreateStudentForm
from students.forms import StudentFilterForm
from students.forms import UpdateStudentForm
from students.models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'templates/students/list.html'
    paginate_by = 12

    def get_filter(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListStudentView, self).get_context_data(**kwargs)
        context['form'] = self.get_filter().form

        return context


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = CreateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
