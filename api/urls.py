from django.urls import path
from . views import ListCustomUsersApiView, ListEquipmentApiView, ListPlanApiView, ListUserPlanApiView


urlpatterns = [
    path('plans', ListPlanApiView.as_view(), name='list-plans'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('equipments', ListEquipmentApiView.as_view(), name='list-equipments'),
    path('subscriptions', ListUserPlanApiView.as_view(), name='list-subscriptions'),
    
]