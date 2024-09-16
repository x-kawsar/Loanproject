from django.shortcuts import render,redirect
from .models import Wing_One
from . forms import Wing_One_Form

def index(request):
    queryset = Wing_One.objects.all()
    context = {'queryset':queryset}
    return render(request, 'index.html', context)


def create_wing_one(request):
    form = Wing_One_Form()
    if request.method == "POST":
        form = Wing_One_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'wing_create.html', context)
