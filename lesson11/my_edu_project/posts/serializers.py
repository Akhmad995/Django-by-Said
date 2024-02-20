from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    text = serializers.CharField()
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Post(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)

        return instance


