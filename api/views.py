from rest_framework.generics import ListAPIView, CreateAPIView
from . serializers import ListCustomUserSerializer, CustomUserSerializer, PlanSerializer, UserPlanSerializer, EquipmentSerializer \
    , CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import CustomUser, Plan, UserPlan, Equipment


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()


class ListEquipmentApiView(ListAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
    permission_classes = [IsAuthenticated]


class ListUserPlanApiView(ListAPIView):
    serializer_class = UserPlanSerializer
    queryset = UserPlan.objects.all()


class ListPlanApiView(ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
