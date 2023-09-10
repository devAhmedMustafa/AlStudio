from rest_framework import serializers
from .models import Design, Album, Like, Save

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'