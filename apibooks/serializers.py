from rest_framework import serializers
from apibooks.models import Books
from django.contrib.auth.models import User


class BooksSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    author = serializers.CharField()
    year = serializers.IntegerField()
    pages = serializers.IntegerField()
    category = serializers.CharField()
    image = serializers.ImageField()


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
