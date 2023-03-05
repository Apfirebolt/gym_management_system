from django.views.generic import ListView, DetailView
from .models import CustomUser, Equipment, UserPlan, Plan
from django.contrib.auth.mixins import LoginRequiredMixin


class ListCustomUsers(ListView):
    """A View to list all the users"""

    model = CustomUser
    template_name = 'core/list_user.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = CustomUser.objects.all().exclude(is_superuser=True)
        return qs


class ListPlan(ListView):
    """A View to list all the plans"""

    model = Plan
    template_name = 'core/list_plan.html'
    context_object_name = 'plans'

    def get_queryset(self):
        qs = Plan.objects.all()
        return qs


class ListEquipment(ListView):
    """A View to list all the equipments"""

    model = Equipment
    template_name = 'core/list_equipment.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        qs = Equipment.objects.all()
        return qs


class ListSubscriptions(ListView):
    """A View to list all the subscriptions"""

    model = UserPlan
    template_name = 'core/list_user_plan.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        if self.request.GET.get('search-input'):
            userEmail = self.request.GET.get('search-input')
            qs = UserPlan.objects.filter(user_id__email__icontains=userEmail).order_by('-subscription_date')
        else:
            qs = UserPlan.objects.all().order_by('-subscription_date')
        return qs


class SubscriptionDetail(DetailView):
    """A View to get detail of a subscription"""

    model = UserPlan
    template_name = 'core/user_plan_detail.html'
    context_object_name = 'subscription'



