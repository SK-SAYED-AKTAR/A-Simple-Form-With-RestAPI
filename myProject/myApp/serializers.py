from rest_framework import serializers
from .models import UserInformation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"