from django.forms import ModelForm

from marketapp.models import Market


class MarketCreationForm(ModelForm):
    #season(날짜 기준)

    class Meta:
        model = Market
        fields = ['market_date','price']
class MarketUpdateForm(ModelForm):

    class Meta:
        model = Market
        fields = ['market_date','price']