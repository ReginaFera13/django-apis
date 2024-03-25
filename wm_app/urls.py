from django.urls import path
from .views import Title_details

urlpatterns = [
    path('<int:title_id>/', Title_details.as_view(), name='title_details'),
]