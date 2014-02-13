from rest_framework import serializers

from bookreview.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """
    Interacting with the AuthorSerializer...
    """
    first_name = serializers.Field(source='first_name')
    last_name = serializers.Field(source='last_name')

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')
