from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    birth_date = serializers.DateField()
    
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_image', 'location', 'birth_date']
        extra_kwargs = {
            'email': {'required': True},
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
