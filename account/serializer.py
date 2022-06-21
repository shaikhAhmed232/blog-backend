from django.contrib.auth.hashers import make_password
from django.forms import ValidationError

from rest_framework import serializers
from .models import CustomUser

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'confirm_password', 'first_name', 'last_name', 'number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate(self, attrs):
        password = attrs.get('password')
        conf_password = attrs.get('confirm_password')
        if password != conf_password:
            raise ValidationError('both passwords are not matching')
        return super().validate(attrs)