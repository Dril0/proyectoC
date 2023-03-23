from django.db import models
from django.urls import (
    reverse,
)  # nos permite referenciarnos a un objeto por su URL template name.

# Create your models here.


class Post(models.Model):
    """creamos una subclase de models.Model 'Post'"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):  # para poder ponerle un titulo al djangoshell/admin
        return self.title

    def get_absolute_url(self):  # usa el url nombrado post_detail y lo pasa al pk
        return reverse("post_detail", kwargs={"pk": self.pk})
