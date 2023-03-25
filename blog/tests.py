from django.test import TestCase
from django.contrib.auth import get_user_model  # nos permite referirnos a nuestro user.
from .models import Post

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
