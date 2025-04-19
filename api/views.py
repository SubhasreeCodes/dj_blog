from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Blog
from api.serializers import BlogSerializer

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer