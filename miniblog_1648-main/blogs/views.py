from django.shortcuts import render
from .models import Blog
# Create your views here.
def home_page(request):
    bloglar = Blog.objects.all()
    context = {
        'blogs': bloglar
    }
    return render(request, 'blog.html', context)