from django.views.generic import ListView
from .models import CustomUser, Equipment, UserPlan, Plan
from django.contrib.auth.mixins import LoginRequiredMixin


class ListCustomUsers(ListView):
    """A View to list all the users"""

    model = CustomUser
    template_name = 'core/list_user.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = CustomUser.objects.all()
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
        qs = UserPlan.objects.all()
        return qs


