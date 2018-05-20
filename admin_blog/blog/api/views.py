from rest_framework.generics import( 
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
    )x
from blog.api.models import Post
from .serializers import PostSerializer
from django.db.models import Q

class PostCreateView(CreateAPIView):
    ueryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(author__icontains=query)).distinct()
        return queryset_list

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer