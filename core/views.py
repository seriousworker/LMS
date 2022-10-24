from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, '../templates/index.html')


class CustomUpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    @classmethod
    def update(cls, request, pk):
        obj = get_object_or_404(cls.model, pk=pk)

        if request.method == 'POST':
            form = cls.form_class(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(cls.success_url))

        form = cls.form_class(instance=obj)

        return render(request, cls.template_name, {'form': form})
