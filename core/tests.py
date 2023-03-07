from django.test import TestCase
from . models import Equipment, Plan
from django.core.files.uploadedfile import SimpleUploadedFile

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)

class EquipmentModelTestCase(TestCase):
    def test_add_equipment(self):
        """Equipment test"""
        equipment = Equipment.objects.create(
            name="New Equipment",
            per_unit_price=10.0,
            quantity = 5,
            image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        )

        equipment.save()
        self.assertEqual(equipment.name, "New Equipment")
        self.assertEqual(equipment.per_unit_price, 10.0)
        self.assertEqual(equipment.quantity, 5)



class PlanModelTestCase(TestCase):
    def test_add_plan(self):
        """Plan test"""
        plan = Plan.objects.create(
            name="New Plan",
            fees=1000.00,
            discount = 15.00,
            description = "A new plan",
            billing_duration = "Monthly",
            image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        )

        plan.save()
        self.assertEqual(plan.name, "New Plan")
        self.assertEqual(plan.fees, 1000.00)
        self.assertEqual(plan.discount, 15.00)
        self.assertEqual(plan.description, "A new plan")
        self.assertEqual(plan.billing_duration, "Monthly")

