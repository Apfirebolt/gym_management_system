from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from gym_management_system.settings import AUTH_USER_MODEL


BILLING_DURATION_CHOICES = (
    ("MONTHLY", "Monthly"),
    ("QUARTERLY", "Quarterly"),
    ("HALF YEARLY", "Half Yearly"),
    ("YEARLY", "Yearly"),
)


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True, max_length=255, blank=True, null=True)
    username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
    profile_image = models.FileField(upload_to='profile_image', blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('Super User', default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "User"



class Plan(models.Model):
    name = models.CharField(max_length=255)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    billing_duration = models.CharField("Billing Duration", max_length=50, choices=BILLING_DURATION_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='plan_images')
    

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Plan"


class UserPlan(models.Model):
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    subscription_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '(%s, %s)' % (self.user_id.email, self.plan_id.name)

    class Meta:
        verbose_name_plural = "User Subscription Plans"
