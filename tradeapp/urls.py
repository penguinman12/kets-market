from django.urls import path
from django.views.generic import TemplateView

from tradeapp.views import TradeCreateView, TradeDetailView

app_name = 'tradeapp'

urlpatterns = [
    path('create/', TradeCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TradeDetailView.as_view(), name='detail'),
    path('list/', TradeDetailView.as_view(), name='list'),
]