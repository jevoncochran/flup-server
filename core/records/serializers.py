from .models import Application
from rest_framework import serializers

class ApplicationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "date", "company", "position", "employment_status", "salary_min", "salary_max", "location", "is_confirmed", "source", "link", "follow_up_date_1", "follow_up_date_2", "has_received_response", "has_received_interview_invitation", "was_rejected", "notes", "user"]
        extra_kwargs = {"user": {"read_only": True}}