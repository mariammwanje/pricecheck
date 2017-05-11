
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, CreateView, RedirectView
from .forms import UserCreateForm


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        return super(SignupView, self).dispatch(request, *args, **kwargs)

signup = SignupView.as_view()


class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url =   reverse_lazy('home')
    form_class = AuthenticationForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
        #return HttpResponseRedirect(self.get_success_url())


class LogoutView(RedirectView):
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

