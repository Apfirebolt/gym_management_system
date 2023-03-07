from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . serializers import ListCustomUserSerializer, PlanSerializer, UserPlanSerializer, EquipmentSerializer \
    , CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import CustomUser, Plan, UserPlan, Equipment


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()


class ListEquipmentApiView(ListAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class ListUserPlanApiView(ListAPIView):
    serializer_class = UserPlanSerializer
    queryset = UserPlan.objects.all()


class ListPlanApiView(ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
