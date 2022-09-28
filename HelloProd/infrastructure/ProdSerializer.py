from datetime import datetime

from rest_framework import serializers

from .models import MyProd


class productDetail:
    def __init__(self, name, amount, place, delete_able=True):
        self.name = name
        self.amount = amount
        self.place = place
        self.create_date = datetime.now()
        self.delete_able = delete_able


class ProdSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, required=True)
    amount = serializers.IntegerField(min_value=0, required=True)
    place = serializers.CharField(required=False)
    delete_able = serializers.BooleanField(required=True)

    class Meta:
        model = MyProd
        fields = "__all__"

    def create(self, validated_data):
        return MyProd.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.place = validated_data.get("place", instance.place)
        instance.delete_able = validated_data.get(
            "delete_able", instance.delete_able)
        instance.save()
        return instance
