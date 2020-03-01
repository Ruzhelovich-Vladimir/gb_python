from django.urls import path
from good.views import list, add

app_name = 'good'

urlpatterns = [
     path('', list , name='list'),
     path('add', add, name='add'),
]

