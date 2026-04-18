from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country, FavoriteCountry, UserPreference, Region
from .serializers import (
    RegisterSerializer,
    MatchRequestSerializer,
    CountrySerializer,
    FavoriteCountrySerializer
)


@api_view(['GET'])
@permission_classes([AllowAny])
def country_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=404)

    serializer = CountrySerializer(country)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=201)
    return Response(serializer.errors, status=400)


class FavoriteListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorites = FavoriteCountry.objects.filter(user=request.user)
        serializer = FavoriteCountrySerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = FavoriteCountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FavoriteDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            favorite = FavoriteCountry.objects.get(pk=pk, user=request.user)
        except FavoriteCountry.DoesNotExist:
            return Response({'error': 'Favorite not found'}, status=404)

        favorite.delete()
        return Response({'message': 'Favorite deleted'}, status=200)


class PreferenceListCreateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        preferences = UserPreference.objects.filter(user=request.user)
        data = []
        for pref in preferences:
            data.append({
                'id': pref.id,
                'current_country': pref.current_country,
                'preferred_region': pref.preferred_region.name if pref.preferred_region else None,
                'safety_weight': pref.safety_weight,
                'salary_weight': pref.salary_weight,
                'quality_weight': pref.quality_weight,
            })
        return Response(data)

    def post(self, request):
        region = None
        region_id = request.data.get('preferred_region_id')
        if region_id:
            try:
                region = Region.objects.get(id=region_id)
            except Region.DoesNotExist:
                return Response({'error': 'Region not found'}, status=404)

        pref = UserPreference.objects.create(
            user=request.user,
            current_country=request.data.get('current_country', ''),
            preferred_region=region,
            safety_weight=request.data.get('safety_weight', 5),
            salary_weight=request.data.get('salary_weight', 5),
            quality_weight=request.data.get('quality_weight', 5),
        )

        return Response({'message': 'Preference created', 'id': pref.id}, status=201)

    def put(self, request, pk):
        try:
            pref = UserPreference.objects.get(pk=pk, user=request.user)
        except UserPreference.DoesNotExist:
            return Response({'error': 'Preference not found'}, status=404)

        region_id = request.data.get('preferred_region_id')
        if region_id:
            try:
                pref.preferred_region = Region.objects.get(id=region_id)
            except Region.DoesNotExist:
                return Response({'error': 'Region not found'}, status=404)

        pref.current_country = request.data.get('current_country', pref.current_country)
        pref.safety_weight = request.data.get('safety_weight', pref.safety_weight)
        pref.salary_weight = request.data.get('salary_weight', pref.salary_weight)
        pref.quality_weight = request.data.get('quality_weight', pref.quality_weight)
        pref.save()

        return Response({'message': 'Preference updated'})


class MatchCountriesView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = MatchRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        preferred_region_id = serializer.validated_data.get('preferred_region_id')
        safety_weight = serializer.validated_data['safety_weight']
        salary_weight = serializer.validated_data['salary_weight']
        quality_weight = serializer.validated_data['quality_weight']

        countries = Country.objects.all()
        if preferred_region_id:
            countries = countries.filter(region_id=preferred_region_id)

        result = []
        for country in countries:
            match_score = (
                country.safety * safety_weight +
                country.salary * salary_weight +
                country.quality_of_life * quality_weight
            )
            result.append({
                'id': country.id,
                'name': country.name,
                'capital': country.capital,
                'region': country.region.name,
                'description': country.description,
                'match_score': match_score,
                'safety': country.safety,
                'salary': country.salary,
                'quality_of_life': country.quality_of_life,
            })

        result.sort(key=lambda x: x['match_score'], reverse=True)
        return Response(result)