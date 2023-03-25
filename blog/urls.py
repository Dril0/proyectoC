from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
)  # importamos las funciones que quermos utilizar

urlpatterns = [
    path(
        "post/<int:pk>", BlogDetailView.as_view(), name="post_detail"
    ),  # pk es el id que agrega django a la database, es un entero por eso <int:pk>
    path(
        "", BlogListView.as_view(), name="home"
    ),  # creamos una ruta vacia a view, con el name home
]
