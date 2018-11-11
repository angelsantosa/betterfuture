from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class AbstractUserLoginTest(UserPassesTestMixin):
    """docstring for AbstractUserLoginTest."""

    login_url = reverse_lazy('account_login')

    pk_url_kwarg = 'pk'

    text_404 = 'No existe'

    redirect_field_name = 'next'

    no_permission_url = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_not_logged()

        user_test_result = self.get_test_func()()
        if not user_test_result:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        if self.no_permission_url:
            return redirect(self.no_permission_url)
        else:
            raise Http404(self.text_404)

    def handle_not_logged(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(self.login_url)


class LoginRequired(LoginRequiredMixin):

    login_url = reverse_lazy('account_login')
    redirect_field_name = 'next'
