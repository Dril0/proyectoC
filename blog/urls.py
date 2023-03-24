from django.urls import path
from .views import BlogListView  # importamos las funciones que quermos utilizar

urlpatterns = [
    path(
        "", BlogListView.as_view(), name="home"
    )  # creamos una ruta vacia a view, con el name home
]
