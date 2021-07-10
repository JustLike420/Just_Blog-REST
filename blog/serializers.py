from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'category')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'text', 'post')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True,
                                            many=True)  # title - поле в модели категории которые должно выводиться
    tags = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
