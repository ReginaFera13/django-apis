from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from django_apis_proj.settings import env

# Create your views here.
class All_characters(APIView):
    def get(self, request):
        url = " https://the-one-api.dev/v2/character"
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {env.get("LOTR_KEY")}'
        }
        response = requests.get(url, headers=headers)
        responseJSON = response.json()
        return Response(responseJSON)