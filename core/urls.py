from django.urls import path, include
from . views import ListCustomUsers, ListPlan, ListEquipment, ListSubscriptions


urlpatterns = [
    path('plans', ListPlan.as_view(), name='list-plans'),
    path('users', ListCustomUsers.as_view(), name='list-users'),
    path('equipments', ListEquipment.as_view(), name='list-equipments'),
    path('subscriptions', ListSubscriptions.as_view(), name='list-subscriptions'),
]