from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html'
    )

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code',
                  'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


# """
# It's important to remember that ModelSerializer classes don't do anything
# particulatly magical, they are simply a shortcut for creating serializer
# classes.
# - An automatically determined set of fields
# - Simple default implementations for the create() and update() methods
# """
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'owner',
#                   'style']


# class UserSerializer(serializers.ModelSerializer):
#     """
#     Because 'snippets' is a reverse relationship on the User model, it will
#     not be included by default when using the ModelSerializer class, so we
#     need to add an explicit field for it.
#     """
#     snippets = serializers.PrimaryKeyRelatedField(many=True,
#                                                   queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']
