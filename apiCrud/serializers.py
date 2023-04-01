from rest_framework import serializers
from .models import VCard
class VCardSericlizer(serializers.ModelSerializer):
    class Meta:
        model=VCard
        fields="__all__"