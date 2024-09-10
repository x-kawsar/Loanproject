from django.shortcuts import render
from .models import Wing_One

def index(request):
    queryset = Wing_One.objects.all()
    context = {'queryset':queryset}
    return render(request, 'index.html', context)
