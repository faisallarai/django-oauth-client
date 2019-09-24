import requests
from django.shortcuts import render
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
)
from .provider import CustomOAuth2Provider
from django.conf import settings


class CustomOAuth2Adapter(OAuth2Adapter):
    provider_id = CustomOAuth2Provider.id

    access_token_url = '{}/o/token/'.format(settings.OAUTH_SERVER_BASEURL)
    profile_url = '{}/accounts/profile/'.format(settings.OAUTH_SERVER_BASEURL)
    
    authorize_url = '{}/o/authorize/'.format(settings.OAUTH_SERVER_BASEURL)

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        print('token-faisal',token.token)
        print('resp-faisal',resp)
        extra_data = resp.json()
        print('extra',extra_data)
        return self.get_provider().sociallogin_from_response(request, extra_data)

oauth2_login = OAuth2LoginView.adapter_view(CustomOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomOAuth2Adapter)
