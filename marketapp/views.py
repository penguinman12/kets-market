from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView,ListView


# Create your views here.
class MarketListView(ListView):
    model = User
    context_object_name = 'target_user'
    template_name = 'marketapp/market.html'

    paginate_by = 25