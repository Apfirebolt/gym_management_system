from django.urls import path
from .views import (
    ListCustomUsersApiView,
    ListCreateEquipmentApiView,
    RetrieveUpdateDestroyEquipmentApiView,
    CreateCustomUserApiView,
    ListPlanApiView,
    ListUserPlanApiView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register", CreateCustomUserApiView.as_view(), name="signup"),
    path("login", TokenObtainPairView.as_view(), name="signin"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    path("plans", ListPlanApiView.as_view(), name="list-plans"),
    path("users", ListCustomUsersApiView.as_view(), name="list-users"),
    path("equipments", ListCreateEquipmentApiView.as_view(), name="list-equipments"),
    path("equipments/<int:pk>", RetrieveUpdateDestroyEquipmentApiView.as_view(), name="detail-equipments"),
    path("subscriptions", ListUserPlanApiView.as_view(), name="list-subscriptions"),
]
