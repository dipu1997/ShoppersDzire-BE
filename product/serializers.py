from rest_framework import serializers

from product.models import Product, ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'size', 'color', 'color_code']

    def create(self, validated_data):
        variant = ProductVariant.objects.create(**validated_data)
        return variant

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.color = validated_data.get('color', instance.color)
        instance.color_code = validated_data.get('color_code', instance.color_code)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    variant = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'image', 'gender', 'variant']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.sku = validated_data.get('sku', instance.sku)
        instance.image = validated_data.get('image', instance.image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
