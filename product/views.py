from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
)

from .models import Product, ProductVariant, Category
from .serializers import ProductSerializer, ProductVariantSerializer, CategorySerializer


@csrf_exempt
@api_view(["GET"])
def all_product(request):
    json = {}
    json_array = []

    product_list = Product.objects.all()

    for product in product_list:
        product_serializer = ProductSerializer(product)
        json_array.append(product_serializer.data)

    json['product'] = json_array
    return Response(json, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def product_by_id(request, pk):
    product = Product.objects.get(pk=pk)
    product_serializer = ProductSerializer(product)

    if not product:
        return Response({
            'error': 'No product found'
        }, status=HTTP_404_NOT_FOUND)

    return Response(product_serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def all_variant(request):
    json = {}
    json_array = []

    variant_list = ProductVariant.objects.all()

    if variant_list is None:
        return Response({
            'error': 'No product variants found'
        }, status=HTTP_404_NOT_FOUND)

    for variant in variant_list:
        variant_serializer = ProductVariantSerializer(variant)
        json_array.append(variant_serializer.data)

    json['variant'] = json_array
    return Response(json, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def variant_by_id(request, pk):
    variant = ProductVariant.objects.get(pk=pk)

    if variant is None:
        return Response({
            'error': 'No variant found'
        }, status=HTTP_404_NOT_FOUND)

    variant_serializer = ProductVariantSerializer(variant)
    return Response(variant_serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def all_categories(request):
    categories = Category.objects.all()
    json_array = []
    json = {}

    if categories is None:
        return Response({
            'error': 'No categories found'
        }, status=HTTP_404_NOT_FOUND)

    for category in categories:
        category_serializer = CategorySerializer(category)
        json_array.append(category_serializer.data)

    json['category'] = json_array
    return Response(json, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def category_by_id(request, pk):
    category = Category.objects.get(pk=pk)

    if category is None:
        return Response({
            'error': 'No category found'
        }, status=HTTP_404_NOT_FOUND)

    category_serializer = CategorySerializer(category)
    return Response(category_serializer.data, status=HTTP_200_OK)
