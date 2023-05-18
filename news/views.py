from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import BasicAuthentication,TokenAuthentication,SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import News,NewsStatus,Status,Comment,CommentStatus
from .serializers import NewsSerializer,NewsStatusSerializer,StatusSerializer,CommentStatusSerializer,CommentSerializer
from .permissions import IsAuthorOrIsAuthenticated,IsAdminOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated, ]
    pagination_class = LimitOffsetPagination
    search_fields=['title']
    ordering_fields=['created']


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news__id=self.kwargs['news_id'])


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class NewsStatusAPIView(APIView):

    def get(self,request,news_id,status_id):
        try:
            news=News.objects.get(pk=news_id)
            news_status=Status.objects.get(pk=status_id)
            if NewsStatus.objects.filter(news=news, author=request.user.author, status=news_status).exists():
                return Response({"error": "You already added this status"})
            NewsStatus.objects.create(author=request.user.author,news=news,status=news_status)
            return Response({"message": "Status added"})
        except Exception as e:
            return Response({"error": "News not found"})







