from django.contrib import admin
from core.models import CustomUser, Plan, Equipment, UserPlan


admin.site.register(CustomUser)
admin.site.register(Plan)
admin.site.register(Equipment)
admin.site.register(UserPlan)
