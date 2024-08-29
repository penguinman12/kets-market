from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from marketapp.decorators import market_delete_required
from marketapp.forms import MarketCreationForm, MarketUpdateForm
from marketapp.models import Market


# Create your views here.



class MarketCreateView(CreateView):
    models = Market
    context_object_name = 'market'
    form_class = MarketCreationForm
    template_name = 'marketapp/create.html'

    success_url = reverse_lazy('marketapp:marketlist')

class MarketUpdateView(UpdateView):
    model = Market
    context_object_name = 'target_market'
    form_class = MarketUpdateForm
    template_name = 'marketapp/update.html'
    success_url = reverse_lazy('marketapp:marketlist')

@method_decorator(market_delete_required,'get')
@method_decorator(market_delete_required,'post')
class MarketDeleteView(DeleteView):
    model = Market
    context_object_name = 'target_market'
    success_url = reverse_lazy('marketapp:marketlist')
class MarketListView(ListView):
    model = Market
    context_object_name = 'market_list'
    template_name = 'marketapp/marketlist.html'

    paginate_by = 25

class MarketSecretView(ListView):
    model = Market
    context_object_name = 'market_secret_list'
    template_name = 'marketapp/market.html'

    paginate_by = 25

