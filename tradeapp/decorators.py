from django.http import HttpResponseForbidden

from tradeapp.models import Trade


def trade_ownership_required(func):
    def decorated(request, *args, **kwargs):
        trade = Trade.objects.get(pk=kwargs['pk'])
        if not trade.trader == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

def trade_delete_required(func):
    def decorated(request, *args, **kwargs):
        trade = Trade.objects.get(pk=kwargs['pk'])

        return func(request, *args, **kwargs)
    return decorated
