from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Paragraph

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'dob', 'created_at', 'modified_at', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user instance.
        """
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        if password:
            user.password = make_password(password)
            user.save()
        return user

class ParagraphSerializer(serializers.ModelSerializer):
    """
    Serializer for the Paragraph model.
    """

    class Meta:
        model = Paragraph
        fields = ['id', 'text']
