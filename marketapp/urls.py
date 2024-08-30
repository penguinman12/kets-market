from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from marketapp.views import MarketListView, MarketCreateView, MarketUpdateView, MarketDeleteView, \
    MarketSecretView, MarketDetailView

app_name = "marketapp"

urlpatterns = [
    path('marketlist/',MarketListView.as_view(), name='marketlist'), # 사용자들이 보는 곳
    path('create/',MarketCreateView.as_view(), name='create'),
    path('update/<int:pk>',MarketUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',MarketDeleteView.as_view(), name='delete'),
    path('marketsecret/',MarketSecretView.as_view(), name='marketsecret'), # 관리자 접근 가능 버튼 제공
    path('detail/<int:pk>',MarketDetailView.as_view(), name='detail')
]