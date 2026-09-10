from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'slug', 'short_description', 'full_description', 'icon', 'image', 'is_featured', 'order')