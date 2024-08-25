from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView,ListView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from tradeapp.models import Trade
from tradeapp.decorators import trade_ownership_required
from tradeapp.forms import TradeCreationForm
# Create your views here.
class TradeCreateView(CreateView):
    model = Trade
    form_class = TradeCreationForm
    template_name= 'tradeapp/create.html'

    def form_valid(self, form):
        temp_trade = form.save(commit=False)
        temp_trade.writer = self.request.user
        temp_trade.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tradeapp:detail', kwargs={'pk': self.object.pk})
class TradeDetailView(DetailView):
    model = Trade
    context_object_name = 'target_trade'
    template_name = 'tradeapp/detail.html'
    paginate_by = 25



class TradeListView(ListView):
    model = Trade
    context_object_name = 'trade_list'
    template_name = 'tradeapp/list.html'
    paginate_by = 50

    def get_queryset(self):
        return Trade.objects.all().order_by('-traded_at')


