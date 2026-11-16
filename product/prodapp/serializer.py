from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer):
    stock_status=serializers.SerializerMethodField()
    class Meta:
        model=ProductModel
        fields="__all__"
        read_only_fields=['id','created_at','owner']


    def validate_price(self,value):
        if value<0:
            raise serializers.ValidationError("price cannot be negative")
        return value

    def get_stock_status(self,value):
        if value.stock>10:
            return "Available"
        elif value.stock>=1:
            return "Low Stock"
        else:
            return "Out of Stock"
