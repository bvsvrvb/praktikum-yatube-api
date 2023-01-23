from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ValidationError, CurrentUserDefault

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate(self, data):
        if self.context.get('request').user == data.get('following'):
            raise ValidationError('Нельзя подписаться на себя')
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            ),
        )
