from django.urls import path, include
from . views import ListCustomUsers, ListPlan


urlpatterns = [
    path('plans', ListPlan.as_view(), name='list-plans'),
    path('users', ListCustomUsers.as_view(), name='list-users'),
]