from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Requisite, PaymentRequest
from .forms import UserForm

User = get_user_model()


class PaymentPage(LoginRequiredMixin, ListView):
    template_name = 'request/payment.html'
    model = PaymentRequest
    paginate_by = 10

    def get_queryset(self):
        return PaymentRequest.objects.select_related(
            'requisites'
        )


class RequsitePage(ListView):
    template_name = 'request/requsite.html'
    model = Requisite
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        order_by = self.request.GET.get('order_by')
        if q:
            q_lst = q.split(",")
            return queryset.filter(Q(payment_type__in=q_lst) |
                                   Q(account_type__in=q_lst) |
                                   Q(first_name__in=q_lst) |
                                   Q(last_name__in=q_lst) |
                                   Q(phone_number__in=q_lst)
                                   )
        if order_by:
            return queryset.order_by(order_by)
        return queryset


class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'request/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(
            User, username=self.kwargs['username'])
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'request/user.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User)

    def get_success_url(self) -> str:
        return reverse_lazy('request:profile')
