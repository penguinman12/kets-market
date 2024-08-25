from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from marketapp.views import MarketListView

app_name = "marketapp"

urlpatterns = [
    path('market/', MarketListView.as_view(), name='market'),
]