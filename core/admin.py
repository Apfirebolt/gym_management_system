from django.contrib import admin
from core.models import CustomUser, Plan, Equipment, UserPlan

class UserAdminPanel(admin.ModelAdmin):
    list_filter = ('email', 'username',)


class EquipmentAdminPanel(admin.ModelAdmin):
    list_filter = ('name',)


class PlanAdminPanel(admin.ModelAdmin):
    list_filter = ('name', 'fees',)


class UserPlanAdminPanel(admin.ModelAdmin):
    list_filter = ('subscription_date', 'is_paid',)


admin.site.register(CustomUser, UserAdminPanel)
admin.site.register(Plan, PlanAdminPanel)
admin.site.register(Equipment, EquipmentAdminPanel)
admin.site.register(UserPlan, UserPlanAdminPanel)
