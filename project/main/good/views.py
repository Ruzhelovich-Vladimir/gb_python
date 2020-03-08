from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from good.models import good
from good.forms import GoodForm


def list(request):
    return render(request, 'good/list_form.html', {'goods': good.objects.all()})

def add(request):
    data = dict()
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
            data['is_valid'] = True
            goods = good.objects.all()
            data['list_html'] = render_to_string('good/partial_goods_list.html', {'goods': goods})
        else:
            data['form_html'] = render_to_string('good/add_form.html', {'form': form}, request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('good/add_form.html', {'form': GoodForm()}, request=request)

    return JsonResponse(data)

