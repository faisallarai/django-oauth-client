from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import CustomOAuth2Provider

urlpatterns = default_urlpatterns(CustomOAuth2Provider)