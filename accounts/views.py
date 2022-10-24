from accounts.forms import ProfileUpdateForm
from accounts.forms import UserRegisterForm
from accounts.forms import UserUpdateForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView


class AccountRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')

        if param_next:
            return param_next

        return reverse('home')


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


@login_required
def account_view(request):
    return render(request, 'accounts/profile_view.html')


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(
            request,
            'accounts/update.html',
            {
                'user_form': user_form,
                'profile_form': profile_form
            }
        )

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile_view'))
