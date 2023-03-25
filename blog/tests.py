from django.test import TestCase
from django.contrib.auth import get_user_model  # nos permite referirnos a nuestro user.
from .models import Post
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="proyectoC", body="el mejor proyecto", author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "proyectoC")
        self.assertEqual(self.post.body, "el mejor proyecto")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "proyectoC")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exist_at_correct_location_listview(self):  # verifica que exista home
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_detailview(
        self,
    ):  # verifica que exista post_detail
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))  # verifica que use el url home
        self.assertEqual(response.status_code, 200)  # retorne un 200 status code
        self.assertContains(
            response, "el mejor proyecto"
        )  # coincide el contenido con el que creamos en SetUpTestData
        self.assertTemplateUsed(
            response, "home.html"
        )  # utiliza el home.html correctamente

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get(
            "/post/10000/"
        )  # no necesitamos un response al post numero 10000 porque no tenemos tantos, y evitamos el 404 http.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "proyectoC")
        self.assertTemplateUsed(response, "post_detail.html")
