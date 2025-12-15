from rest_framework import serializers
from ..models import User
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')