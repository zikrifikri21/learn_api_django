from rest_framework import viewsets,status
from rest_framework.decorators import action
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

class BookViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'], url_path='s/(?P<slug>[-\w]+)')
    @csrf_exempt
    def get_by_slug(self, request, slug=None):
        if not slug:
            return Response({'error': 'Slug parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        book = Post.objects.filter(slug=slug).first()
        if not book:
            return Response({'error': 'Buku tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(book)
        return Response(serializer.data)