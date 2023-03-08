from core.models import Equipment, Plan, CustomUser
from .serializers import EquipmentSerializer, PlanSerializer
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


client = APIClient()


class EquipmentTest(TestCase):
    """ Test module for Equipment model """

    def setUp(self):
        user = CustomUser.objects.create(username='john', email='js@js.com', password='js.sj')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        Equipment.objects.create(
            name="New Equipment",
            per_unit_price=10.0,
            quantity = 5,
            
        )

        Equipment.objects.create(
            name="Another New Equipment",
            per_unit_price=16.0,
            quantity = 2,
            
        )


    def test_get_all_equipments(self):
        # get API response
        response = client.get(reverse('api:list-equipments'))
        # get data from db
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PlanTest(TestCase):
    """ Test module for Plan model """

    def setUp(self):
        Plan.objects.create(
            name="New Plan",
            fees=1000.0,
            discount = 15.0,
            description = "A new plan",
            billing_duration = "Monthly",
        )

        Plan.objects.create(
            name="Another New Plan",
            fees=1500.0,
            discount = 15.0,
            description = "Another new plan",
            billing_duration = "Monthly",
        )


    def test_get_all_plans(self):
        # get API response
        response = client.get(reverse('api:list-plans'))
        # get data from db
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)