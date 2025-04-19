from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from backend.models import Blog


# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'frontend/home.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'frontend/detail.html', {'blog': blog})