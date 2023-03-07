from core.models import Equipment, Plan
from .serializers import EquipmentSerializer, PlanSerializer
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


client = Client()


class EquipmentTest(TestCase):
    """ Test module for Equipment model """

    def setUp(self):
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