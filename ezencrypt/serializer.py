from rest_framework import serializers

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    algo = serializers.CharField()
    password = serializers.CharField()
