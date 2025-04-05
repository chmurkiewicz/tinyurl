from django.conf import settings
from rest_framework import serializers

from tinyurl.models import Link


class LinkSerializer(serializers.ModelSerializer):

    original_url = serializers.URLField(max_length=settings.MAX_URL_LENGTH, write_only=True)

    class Meta:
        model = Link
        fields = ("original_url", "short_url")
