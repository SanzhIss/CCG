from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    CreateUserView,
    UserInfoView,
    UserUpdateView
)

urlpatterns = [
    path('create-user/', CreateUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', UserInfoView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
]
