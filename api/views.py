from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from drf_spectacular.utils import extend_schema, extend_schema_view
from . serializers import ListCustomUserSerializer, CustomUserSerializer, PlanSerializer, UserPlanSerializer, EquipmentSerializer \
    , CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import CustomUser, Plan, UserPlan, Equipment
from rest_framework import generics, parsers


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = []
    permission_classes = []

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    authentication_classes = []
    permission_classes = []


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()


@extend_schema_view(
    get=extend_schema(
        summary="List all equipment",
        description="Retrieve a paginated list of all gym equipment.",
    ),
    post=extend_schema(
        summary="Create new equipment",
        description="Upload a new equipment item with an optional image asset (ImageKit).",
    ),
)
class ListCreateEquipmentApiView(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser,
    ]


@extend_schema_view(
    get=extend_schema(summary="Retrieve equipment by ID"),
    put=extend_schema(summary="Update equipment"),
    patch=extend_schema(summary="Partially update equipment / replace image"),
    delete=extend_schema(summary="Delete equipment and remote ImageKit asset"),
)
class RetrieveUpdateDestroyEquipmentApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser,
    ]


class ListUserPlanApiView(ListAPIView):
    serializer_class = UserPlanSerializer
    queryset = UserPlan.objects.all()


class ListPlanApiView(ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
