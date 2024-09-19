
from django.shortcuts import render
from .models import ScrapedData

def index(request):
    data = ScrapedData.objects.all()
    return render(request, 'scrape/index.html', {'data': data})


