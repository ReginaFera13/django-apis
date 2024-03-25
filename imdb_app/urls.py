from django.urls import path
from .views import Coming_soon

urlpatterns = [
    path('', Coming_soon.as_view(), name='coming_soon'),
]