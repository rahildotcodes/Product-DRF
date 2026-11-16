from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,ListAPIView,DestroyAPIView
from prodapp.serializer import ProductSerializer
from rest_framework import authentication,permissions
from .models import ProductModel
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CreateListProduct(CreateAPIView,ListAPIView):
    serializer_class=ProductSerializer
    authentication_classes=[authentication.TokenAuthentication]
    pagination_classes=[permissions.IsAuthenticated]
    # queryset=ProductModel.objects.all()
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['category','name']
    ordering_fields=['price']
    filterset_fields=['stock']
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        return ProductModel.objects.filter(owner=self.request.user)

class UpdateRetrieveDeleteView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    serializer_class=ProductSerializer
    authentication_classes=[authentication.TokenAuthentication]
    pagination_classes=[permissions.IsAuthenticated]
    # queryset=ProductModel.objects.all()
    lookup_url_kwarg="id"

    def get_queryset(self):
        return ProductModel.objects.filter(owner=self.request.user)
    

