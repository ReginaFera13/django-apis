from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from django_apis_proj.settings import env

# Create your views here.
class All_characters(APIView):
    def get(self, request):
        url = "https://game-of-thrones1.p.rapidapi.com/Characters"
        headers = {
	        "X-RapidAPI-Key": env.get('GOT_KEY'),
	        "X-RapidAPI-Host": env.get('GOT_HOST')
        }
        response = requests.get(url, headers=headers)
        responseJSON = response.json()
        return Response(responseJSON)