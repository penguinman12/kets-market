from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from marketapp.decorators import market_delete_required
from marketapp.forms import MarketCreationForm, MarketUpdateForm
from marketapp.models import Market


# Create your views here.



class MarketCreateView(CreateView):
    model = Market
    form_class = MarketCreationForm
    template_name = 'marketapp/create.html'

    success_url = reverse_lazy('marketapp:marketsecret')
    def form_valid(self, form):
        temp_market = form.save(commit=False)
        temp_market.save()
        return super().form_valid(form)
class MarketUpdateView(UpdateView):
    model = Market
    context_object_name = 'target_market'
    form_class = MarketUpdateForm
    template_name = 'marketapp/update.html'
    success_url = reverse_lazy('marketapp:marketsecret')



class MarketDetailView(DetailView):
    model = Market
    context_object_name = 'target_market'
    template_name = 'marketapp/detail.html'
@method_decorator(market_delete_required,'get')
@method_decorator(market_delete_required,'post')
class MarketDeleteView(DeleteView):
    model = Market
    context_object_name = 'target_market'
    success_url = reverse_lazy('marketapp:marketsecret')
    template_name = 'marketapp/delete.html'

class MarketListView(ListView):
    model = Market
    context_object_name = 'market_list'
    template_name = 'marketapp/marketlist.html'

    paginate_by = 25

    def get_queryset(self):
        return Market.objects.all().order_by('-market_date')
class MarketSecretView(ListView):
    model = Market
    context_object_name = 'market_secret_list'
    template_name = 'marketapp/marketsecret.html'

    paginate_by = 25


    def get_queryset(self):
        return Market.objects.all().order_by('-market_date')