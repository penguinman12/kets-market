from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView,ListView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from tradeapp.models import Trade
from tradeapp.decorators import trade_ownership_required,trade_delete_required
from tradeapp.forms import TradeCreationForm,TradeUpdateForm
from django.db import transaction
# Create your views here.
class TradeCreateView(CreateView):
    model = Trade
    form_class = TradeCreationForm
    template_name= 'tradeapp/create.html'

    def form_valid(self, form):
        temp_trade = form.save(commit=False)
        temp_trade.trader = self.request.user
        temp_trade.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tradeapp:detail', kwargs={'pk': self.object.pk})

class TradeUpdateView(UpdateView):
    model = Trade
    context_object_name = 'target_trade'
    form_class = TradeUpdateForm
    template_name = 'tradeapp/update.html'
    success_url = reverse_lazy('tradeapp:list')

    def form_valid(self, form):
        trade = form.save(commit=False)

        with transaction.atomic():
            if trade.trade_type == 'buy' and trade.result:
                # 매수일 경우
                if trade.trader.account.cash >= trade.trading_price:
                    trade.trader.account.cash -= trade.trading_price
                    trade.trader.account.carbon_credits += trade.trading_quantity
                else:
                    raise ValueError("잔액이 부족합니다.")
            elif trade.trade_type == 'sell' and trade.result:
                # 매도일 경우
                if trade.trader.account.carbon_credits >= trade.trading_quantity:
                    trade.trader.account.carbon_credits -= trade.trading_quantity
                    trade.trader.account.cash += trade.trading_price
                else:
                    raise ValueError("탄소 배출권이 부족합니다.")

            trade.trader.account.save()
            trade.save()

        return super().form_valid(form)

class TradeDetailView(DetailView):
    model = Trade
    context_object_name = 'target_trade'
    template_name = 'tradeapp/detail.html'
    paginate_by = 25
@method_decorator(trade_delete_required,'get')
@method_decorator(trade_delete_required,'post')
class TradeDeleteView(DeleteView):
    model = Trade
    context_object_name = 'target_trade'
    success_url = reverse_lazy('tradeapp:list')
    template_name = 'tradeapp/delete.html'
class TradeListView(ListView):
    model = Trade
    context_object_name = 'trade_list'
    template_name = 'tradeapp/list.html'
    paginate_by = 50

class UserTradeListView(ListView):
    model = Trade
    context_object_name = 'trade_user_list'
    template_name = 'tradeapp/user_list.html'
    paginate_by = 50

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Trade.objects.filter(trader=user).order_by('-traded_at')
        else:
            return Trade.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context