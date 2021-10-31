from django.shortcuts import render
from django.views.generic import CreateView
from apps.blogs.forms import CreateBlogForm

# Create your views here.
class BlogCreateView(CreateView):
    form_class = CreateBlogForm
    #model = Blog
    template_name = 'backend/create_update/create.html'
    success_url = '/'
    # queryset = Blog.objects.all()