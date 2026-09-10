from rest_framework import serializers
from .models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image', 'caption')


class ProjectSerializer(serializers.ModelSerializer):
    gallery_images = ProjectImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'client_name', 'category', 'short_description', 'full_description', 'cover_image', 'project_url', 'is_featured', 'order', 'gallery_images')