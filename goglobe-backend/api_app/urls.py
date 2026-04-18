from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    country_list,
    country_detail,
    register_user,
    FavoriteListCreateView,
    FavoriteDeleteView,
    PreferenceListCreateUpdateView,
    MatchCountriesView
)

urlpatterns = [
    path('countries/', country_list),
    path('countries/<int:pk>/', country_detail),

    path('register/', register_user),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('favorites/', FavoriteListCreateView.as_view()),
    path('favorites/<int:pk>/', FavoriteDeleteView.as_view()),

    path('preferences/', PreferenceListCreateUpdateView.as_view()),
    path('preferences/<int:pk>/', PreferenceListCreateUpdateView.as_view()),

    path('matches/', MatchCountriesView.as_view()),
]