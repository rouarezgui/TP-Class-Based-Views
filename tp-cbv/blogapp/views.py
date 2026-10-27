
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import BlogPost


class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'Posts/blogView.html'
    ordering = ['-created_on', '-id']


class BlogCreateWithFields(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author', 'created_on']
    template_name = 'Posts/blogcreate.html'
    success_url = reverse_lazy('listhtml')
