from django.http import Http404
from blog.models.post import Post
from blog.serializers.post_serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostList(APIView):

    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
