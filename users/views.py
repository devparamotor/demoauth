from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Users


class UserViewSet(viewsets.ModelViewSet):
        queryset = Users.objects.all().order_by('user_name')
        serializer_class = UserSerializer

