from django.shortcuts import render

# Create your views here
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('name', 'category', 'subcategory')
