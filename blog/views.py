from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer, CommentCreateSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

class CommentCreateView(APIView):
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)
