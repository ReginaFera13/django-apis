from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
import urllib.request
import json
from django_apis_proj.settings import env

# Create your views here.
class Title_details(APIView):
    def get(self, request, title_id):
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={env.get('WM_KEY')}") as url:
            data = json.loads(url.read().decode())
            # print(data)
            return Response(data)
