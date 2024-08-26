from django.forms import ModelForm

from tradeapp.models import Trade


class TradeCreationForm(ModelForm):
    #season(날짜 기준)

    class Meta:
        model = Trade
        fields = ['trade_type','quantity','price']

class TradeUpdateForm(ModelForm):

    class Meta:
        model = Trade
        fields = ['traded_at','trade_type','quantity','price','result','trading_quantity','trading_price']