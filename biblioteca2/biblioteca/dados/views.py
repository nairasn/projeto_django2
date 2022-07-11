from django.shortcuts import render
from django.utils.decorators import method_decorator
from .models import Cliente
from .serializers import ClienteSerializer
from django.views.decorators.cache import cache_page

from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)
    

cache_page(60*3)
def home(request):
    cliente = Cliente.objects.all()
    return render(request, 'home.html', {'clientes': cliente})