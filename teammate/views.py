from django.shortcuts import render
from rest_framework.relations import ManyRelatedField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class UserModelView(APIView):
    def get(self, request):

        try:
            id = request.query_params["id"]
            if id != None:
                user = UserModel.objects.get(id=id)
                serializer = UserModelSerializer(user)
        except:
            users = UserModel.objects.all()
            serializer = UserModelSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(request, pk=None):
        user = UserModel.objects.get(id=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)


class ProjectModelView(APIView):
    def get(self, request):
        projects = ProjectModel.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
