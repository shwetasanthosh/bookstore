from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apibooks.models import Books
from apibooks.serializers import BooksSerializer
from apibooks.serializers import BookModelSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication, permissions


class BooksView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.all()
        serializer = BooksSerializer(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class BooksDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Books.objects.get(id=id)
        serilizer = BooksSerializer(qs, many=False)
        return Response(data=serilizer.data)

    def put(self, request, *args, **kwargs):
        return Response(data="updating a product")

    def delete(self, request, *args, **kwargs):
        return Response(data="Deleting a product")


class BooksViewsetView(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def list(self, request, *args, **kwargs):
    #     qs = Books.objects.all()
    #     serializer = BookModelSerializer(qs, many=True)
    #     return Response(data=serializer.data)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = BookModelSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     id = kwargs.get("pk")
    #     qs = Books.objects.get(id=id)
    #     serializer = BookModelSerializer(qs, many=False)
    #     return Response(data=serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     id = kwargs.get("pk")
    #     Books.objects.filter(id=id).delete()
    #     return Response("deleted")
    #
    # def update(self, request, *args, **kwargs):
    #     id = kwargs.get("pk")
    #     obj = Books.objects.get(id=id)
    #     serializer = BookModelSerializer(data=request.data,instance = obj)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

    @action(methods=["GET"], detail=False)
    def categories(self, request, *args, **kwargs):
        res = Books.objects.value_list("category", flat=True).distinct()
        return Response(data=res)
