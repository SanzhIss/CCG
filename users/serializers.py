from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'last_login')