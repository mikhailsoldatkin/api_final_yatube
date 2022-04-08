from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, Follow, User


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            slug_field='username',
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(read_only=False,
                                 queryset=User.objects.all(),
                                 slug_field='username')

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Не может быть двух одинаковых подписок!'
            )
        ]

    def validate_following(self, value):
        if self.context.get('request').user == value:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя!')
        return value
