from marketapp.models import Market


def market_delete_required(func):
    def decorated(request, *args, **kwargs):
        market = Market.objects.get(pk=kwargs['pk'])

        return func(request, *args, **kwargs)
    return decorated
