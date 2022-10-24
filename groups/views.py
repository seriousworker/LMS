from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from groups.forms import CreateGroupForm
# from groups.forms import GroupFilterForm
from groups.forms import UpdateGroupForm
from groups.models import Group

from students.models import Student


# def get_group(request):
#     groups = Group.objects.select_related('headman')
#
#     filter_form = GroupFilterForm(data=request.GET, queryset=groups)
#     return render(request,
#                   template_name='templates/groups/list.html',
#                   context={
#                       'title': 'List of groups',
#                       'filter_form': filter_form,
#                   })


class ListGroupView(ListView):
    model = Group
    template_name = 'templates/groups/list.html'
    extra_context = {'title': 'List of groups'}


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


class DetailGroupView(DetailView):
    model = Group
    template_name = 'groups/detail.html'


class UpdateGroupView(UpdateView):
    model = Group
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')
        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        elif pk == 0:
            form.instance.headman = None
        form.save()

        return response


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
