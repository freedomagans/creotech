from rest_framework import serializers
from .models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id', 'name', 'slug', 'role', 'bio', 'photo', 'email', 'linkedin_url', 'twitter_url', 'github_url', 'order')