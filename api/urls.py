from django.urls import path
from . views import ListCustomUsersApiView, ListEquipmentApiView, CreateCustomUserApiView, ListPlanApiView, ListUserPlanApiView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='signup'),
    path('login', obtain_auth_token, name='signin'),
    path('plans', ListPlanApiView.as_view(), name='list-plans'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('equipments', ListEquipmentApiView.as_view(), name='list-equipments'),
    path('subscriptions', ListUserPlanApiView.as_view(), name='list-subscriptions'),
    
]