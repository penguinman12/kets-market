from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from marketapp.views import MarketListView, MarketCreateView, MarketUpdateView, MarketDeleteView,  \
    MarketSecretView

app_name = "marketapp"

urlpatterns = [
    path('marketlist/',MarketSecretView.as_view(), name='marketlist'), # 관리자 접근 가능 버튼 제공
    path('create/',MarketCreateView.as_view(), name='create'),
    path('update/',MarketUpdateView.as_view(), name='update'),
    path('delete/',MarketDeleteView.as_view(), name='delete'),
    path('market/',MarketListView.as_view(), name='market') # 사용자들이 보는 곳
]