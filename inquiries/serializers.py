from rest_framework import serializers
from .models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ('inquiry_type', 'name', 'email', 'phone', 'subject', 'message', 'project_type', 'budget_range', 'timeline')