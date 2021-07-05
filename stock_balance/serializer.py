from rest_framework import serializers
from stock.models import Stock


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.PrimaryKeyRelatedField(queryset=Stock)
    count = serializers.IntegerField()
