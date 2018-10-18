from rest_framework import serializers

from posts.models import Post

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]

post_detail_url = serializers.HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
    )

class PostDetailSerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    html = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
            'image',
            'html',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostListSerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
