from rest_framework import serializers
from .models import address_info


class AddSerializers(serializers.ModelSerializer):
    class Meta:
        model = address_info
        fields = ('id', 'longitude', 'latitude', 'address', 'phone', 'desc')