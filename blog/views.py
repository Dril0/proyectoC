from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)  # importamos Listview y detailview para usar,
from .models import Post

# Create your views here.


class BlogListView(
    ListView
):  # Usamos ListView como subclase y linkeamos el model con el template
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
