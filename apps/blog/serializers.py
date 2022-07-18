from rest_framework import serializers
from .models import Tag, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    # tags = serializers.SerializerMethodField(read_only=True)

    def get_tags(self, obj):
        tags = obj.tags.all()
        serializer = TagSerializer(tags, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'tags', 'content', 'created_at']

    # def create(self, validated_data):
    #     tags = validated_data.pop('tags', [])
    #     instance = Post.objects.create(**validated_data)
    #     for tag in tags:
    #         instance.tags.add(tag)
    #     return instance
