from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.permissions import IsOwner
from users.serializers import (
    CreateUserSerializer,
    UserInfoSerializer,
)

User = get_user_model()


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer


class GetTokenView(APIView):

    def post(self, request):
        refresh = RefreshToken.for_user(self.request.user)

        return Response(data={
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)


class UserInfoView(APIView):
    queryset = User
    serializer_class = UserInfoSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serialize_user = UserInfoSerializer(request.user)

        return Response(data=serialize_user.data, status=status.HTTP_200_OK)


class UserUpdateView(UpdateAPIView):
    serializer_class = UserInfoSerializer
    queryset = User
    permission_classes = (IsOwner, )
