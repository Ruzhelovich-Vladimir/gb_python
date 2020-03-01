from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from good.forms import GoodForm
from good.models import good

def list(request):
    return render(request, 'good/list_form.html', {'goods': good.objects.all()})


def add(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GoodForm()

    return render(request, 'good/add_form.html', {'form': form})

