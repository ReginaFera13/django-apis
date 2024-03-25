from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from django_apis_proj.settings import env

# Create your views here.
class Coming_soon(APIView):
    def get(self, request):
        url = "https://imdb188.p.rapidapi.com/api/v1/getUpcomingMovies"
        querystring = {"region":"US"}
        headers = {
            "X-RapidAPI-Key": env.get('IMDB_KEY'),
            "X-RapidAPI-Host": env.get('IMDB_HOST')
        }
        response = requests.get(url, headers=headers, params=querystring)
        responseJSON = response.json()
        return Response(responseJSON)