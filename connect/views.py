from django.shortcuts import render
from django.http import HttpResponse
from .models import Raw_Ticks

# Create your views here.
def index(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, this view will organise the shortcuts to queries")


def first_tick(request):
    return render(request, 'base.html', {'result':Raw_Ticks.objects.first()})
