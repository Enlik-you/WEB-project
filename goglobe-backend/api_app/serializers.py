from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Country, FavoriteCountry


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class MatchRequestSerializer(serializers.Serializer):
    preferred_region_id = serializers.IntegerField(required=False)
    safety_weight = serializers.IntegerField()
    salary_weight = serializers.IntegerField()
    quality_weight = serializers.IntegerField()


class CountrySerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class FavoriteCountrySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = FavoriteCountry
        fields = '__all__'