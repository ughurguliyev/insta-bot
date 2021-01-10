from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model, login as auth_login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import UserLogInForm, SearchForm
from .actions import CreateSearch
from .models import Search

# Create your views here.

User = get_user_model()


class dashboardPageView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'table_infos': Search.objects.all()
        }

        return context


class loginPageView(FormView):
    form_class = UserLogInForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('dashboard-page')

    def check_user_password(self, form, user):
        password = form.cleaned_data.get('password')
        return user.check_password(password)

    def get_user(self, form):
        username = form.cleaned_data.get('username')
        valid_user = get_object_or_404(
            User.objects.all(),
            username=username
        )
        return valid_user

    def form_valid(self, form):
        user = self.get_user(form=form)
        if user:
            is_valid_password = self.check_user_password(form=form, user=user)
            if is_valid_password:
                auth_login(self.request, user)
                return super().form_valid(form)
        return super().form_valid(form)


class LogoutView(LogoutView):
    def get_next_page(self):
        return reverse('login-page')


class searchFormPageView(FormView):
    template_name = 'dashboard/form.html'
    form_class = SearchForm
    success_url = '/'

    def form_valid(self, form):
        CreateSearch().create(
            username = form.cleaned_data['username'],
            search_title = form.cleaned_data['search_title'],
            note = form.cleaned_data['note']
        )
        return HttpResponseRedirect(self.get_success_url())
