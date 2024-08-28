from django.urls import path
from django.views.generic import TemplateView

from tradeapp.views import TradeCreateView, TradeDetailView, TradeListView, UserTradeListView, TradeDeleteView, \
    TradeUpdateView, UserTradeListView2

app_name = 'tradeapp'



urlpatterns = [
    path('create/', TradeCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TradeDetailView.as_view(), name='detail'),
    path('list/', TradeListView.as_view(), name='list'),
    path('user_list2/<int:pk>', UserTradeListView2.as_view(), name='user_list2'),
    path('user_list/<int:pk>', UserTradeListView.as_view(), name='user_list'),
    path('update/<int:pk>', TradeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TradeDeleteView.as_view(), name='delete'),
]