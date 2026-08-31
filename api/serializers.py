from rest_framework import serializers
from gym_management_system import settings
from core.models import CustomUser, Plan, UserPlan, Equipment
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('No account exists with these credentials, check password and email')
    }

    def validate(self, attrs):
        
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data 
        data.update({'userData': {
            'email': self.user.email,
            'username': self.user.username,
            'id': self.user.id
        }})
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.SerializerMethodField()
    refresh = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'id', 'is_staff', 'password', 'access', 'refresh',)
    
    def get_refresh(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh)

    def get_access(self, user):
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token),
        return access

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ListCustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_staff',)


class PlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plan
        fields = '__all__'
        read_only_fields = ['created_by']


class UserPlanSerializer(serializers.ModelSerializer):

    user_id = ListCustomUserSerializer(read_only=True)

    class Meta:
        model = UserPlan
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Equipment
        fields = [
            "id",
            "name",
            "per_unit_price",
            "quantity",
            "image",
            "image_url",
            "image_file_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "image_url",
            "image_file_id",
            "created_at",
            "updated_at",
        ]

    def _upload_to_imagekit(self, file_obj):
        """Uploads file buffer to ImageKit using v5.x SDK."""
        # Rewind pointer to start of file
        file_obj.seek(0)
        file_bytes = file_obj.read()
        file_name = getattr(file_obj, "name", "equipment_image.jpg")

        # In v5.x, call .files.upload(...)
        upload_response = settings.imagekit_client.files.upload(
            file=file_bytes,
            file_name=file_name,
            folder="/equipment/",
            use_unique_file_name=True,
        )

        return {
            "image_url": getattr(upload_response, "url", None),
            "image_file_id": getattr(
                upload_response, "file_id", getattr(upload_response, "id", None)
            ),
        }

    def create(self, validated_data):
        image_file = validated_data.pop("image", None)
        if image_file:
            uploaded = self._upload_to_imagekit(image_file)
            validated_data["image_url"] = uploaded["image_url"]
            validated_data["image_file_id"] = uploaded["image_file_id"]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image_file = validated_data.pop("image", None)
        if image_file:
            # Delete old image in ImageKit (v5.x: .files.delete)
            if instance.image_file_id:
                try:
                    settings.imagekit_client.files.delete(
                        file_id=instance.image_file_id
                    )
                except Exception as e:
                    print(f"Failed to delete old ImageKit file: {e}")

            # Upload replacement
            uploaded = self._upload_to_imagekit(image_file)
            instance.image_url = uploaded["image_url"]
            instance.image_file_id = uploaded["image_file_id"]

        return super().update(instance, validated_data)
