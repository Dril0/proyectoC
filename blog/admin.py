from django.contrib import admin
from .models import Post  # importamos los modelos que queremos ver en admin.

# Register your models here.

admin.site.register(
    Post
)  # registramos el modelo Post al admin. ahora lo podemos ver ahi.
