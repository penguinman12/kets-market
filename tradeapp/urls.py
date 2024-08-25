from django.urls import path
from django.views.generic import TemplateView

from tradeapp.views import TradeCreateView, TradeDetailView, TradeListView, UserTradeListView

app_name = 'tradeapp'

urlpatterns = [
    path('create/', TradeCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TradeDetailView.as_view(), name='detail'),
    path('list/', TradeListView.as_view(), name='list'),
    path('user_list/<int:pk>', UserTradeListView.as_view(), name='user_list'),
]