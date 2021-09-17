from rest_framework import serializers

from .models import Users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'user_name', 'user_age')