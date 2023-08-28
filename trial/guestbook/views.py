from django.shortcuts import render
from datetime import datetime
from . import models
from .models import Guests
from django.views.generic import CreateView
# Create your views here.

def homepage(request):
    Guests = models.Guests.objects.all()
    return render(request,'guestbook/home.html',{'today':datetime.today,'Guests':Guests})

def home(request):
    return render(request, 'guestbook/bas.html',{})

class GuestsCreateView(CreateView):
    model = Guests
    fields = ['Guestname','time']
    success_url = 'home'

