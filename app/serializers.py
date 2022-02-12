from rest_framework import serializers
from app.models import QRimg


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRimg
        fields = "__all__"

class GenerateSerializer(serializers.Serializer):
    text = serializers.CharField(required = True)